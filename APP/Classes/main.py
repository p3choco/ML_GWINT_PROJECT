import cv2
from ultralytics import YOLO

from APP.Classes.card_factory import CardFactory
from APP.Classes.character import Character
from APP.Classes.row import Row
from APP.Classes.side import Side
from const.models import FIND_SIGN_MODEL_PATH, FIND_CARDS_MODEL_PATH
from models.find_sign_model import FindSignModel
from models.find_cards_model import FindCardsModel
from const.imgs import PLANSZA2


def find_bond_partners(source_card, all_cards_in_row):
    """
    Wyszukuje w rzędzie karty, które mają 'bond' i taką samą siłę jak karta źródłowa.
    """

    source_points = source_card.num_points

    if source_points is None:
        return []

    num_of_partners = 1
    for card_to_check in all_cards_in_row:
        if card_to_check is source_card:
            continue

        if card_to_check.num_points == source_points and card_to_check.bond:
            num_of_partners += 1
    return num_of_partners


def count_points(player):
    all_rows = [
        player.sword_row,
        player.bow_row,
        player.catapult_row
    ]
    points = 0
    hero_points = 0

    for row in all_rows:
        row_points = 0
        for card in row.get_cards():
            if card.num_points is None:
                continue
            local_card_points = card.num_points
            if row.isWeather:
                local_card_points = 1
            if card.high_morale:
                row_points += (len(row.get_cards()) - 1)

            if card.bond:
                num_of_partners = find_bond_partners(card, row.get_cards())
                print("row_points: {}".format(local_card_points * num_of_partners))
                row_points += (local_card_points * num_of_partners)

            elif card.is_hero:
                hero_points += card.num_points
            elif not card.bond:
                row_points += local_card_points

        if row.isHorn:
            row_points *= 2
        points += (row_points + hero_points)
    return points


def checkPlayer():
    #TODO
    return "player1"

def main_pipeline():
    players = {
        "player1": Side({"sword_row": [], "bow_row": [], "catapult_row": [], "no_row": []}),
        "player2": Side({"sword_row": [], "bow_row": [], "catapult_row": [], "no_row": []})
    }
    findCardsModel = FindCardsModel(FIND_CARDS_MODEL_PATH)
    findSignModel = FindSignModel(FIND_SIGN_MODEL_PATH)

    board_image = cv2.imread(PLANSZA2)

    if board_image is None:
        print(f"Błąd: Nie można wczytać obrazu z {PLANSZA2}")
        return

    print("--- ETAP 1: Wykrywanie wszystkich kart na planszy ---")
    # === KROK 2: Uruchomienie pierwszego modelu do lokalizacji kart ===
    # Przekazujemy cały obraz (jako tablicę NumPy) do modelu
    card_detection_results = findCardsModel.predict(board_image)

    # Wyniki są zazwyczaj listą, bierzemy pierwszy element

    if not card_detection_results.boxes:
        print("Nie wykryto żadnych kart na planszy.")
        return

    # === KROK 3: Pętla po każdej wykrytej karcie ===
    for i, box in enumerate(card_detection_results.boxes):
        coords = box.xyxy[0].int().tolist()
        x1, y1, x2, y2 = coords

        # === KROK 4: Wycięcie karty z obrazu (bezpośrednio w pamięci) ===
        cropped_card_image = board_image[y1:y2, x1:x2]

        card_class_name = card_detection_results.names[int(box.cls[0])]
        print(f"--- Analizuję kartę nr {i + 1} (wykryty typ: '{card_class_name}') ---")
        # w zależności jak jest karta tak trza ją obrócić
        cropped_card_image = cv2.rotate(cropped_card_image, cv2.ROTATE_90_COUNTERCLOCKWISE)

        # === KROK 5: Przekazanie wyciętego fragmentu do drugiego modelu ===
        sign_detection_results = findSignModel.predict(cropped_card_image)

        # === KROK 6: Zebranie i wyświetlenie wyników dla tej jednej karty ===
        if sign_detection_results.boxes:
            #narazie mock:
            player = checkPlayer()
            signs = [sign_detection_results.names[int(cls_id)] for cls_id in sign_detection_results.boxes.cls]
            card = CardFactory.create_card(signs)
            #obsługa rogu na karcie

            if card.horn:
                if card.card_row == "miecz":
                    players[player].sword_row.isHorn = True
                elif card.card_row == "lucznik":
                    players[player].bow_row.isHorn = True
                elif card.card_row == "katapulta":
                    players[player].catapult_row.isHorn = True

            annotated_cropped_card = cropped_card_image.copy()
            for sign_box in sign_detection_results.boxes:
                sign_coords = sign_box.xyxy[0].int().tolist()
                sx1, sy1, sx2, sy2 = sign_coords
                sign_class_id = int(sign_box.cls[0])
                sign_class_name = sign_detection_results.names[sign_class_id]
                sign_confidence = float(sign_box.conf[0])

                # Rysowanie prostokąta wokół symbolu na wyciętej karcie
                cv2.rectangle(annotated_cropped_card, (sx1, sy1), (sx2, sy2), (255, 0, 0), 1)

                # Rysowanie tekstu symbolu
                sign_label = f"{sign_class_name} {sign_confidence:.2f}"
                cv2.putText(annotated_cropped_card, sign_label, (sx1, sy1 - 5),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 2)

            # Zapisz wyciętą kartę z naniesionymi symbolami
            output_path_cropped_card = f"./cards/output_card_{i + 1}_with_signs.jpg"
            cv2.imwrite(output_path_cropped_card, annotated_cropped_card)
            row = players[player].findRow(card)
            row.add_card(card)

    print("ilość pkt:" + str(count_points(players['player1'])))
    # count_points(players['player2'])


if __name__ == "__main__":
    main_pipeline()
