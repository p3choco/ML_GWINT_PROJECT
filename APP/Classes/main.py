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


def count_points(cards):
    pass

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

    print(f"Znaleziono {len(card_detection_results.boxes)} kart. Rozpoczynam analizę szczegółową...\n")

    # === KROK 3: Pętla po każdej wykrytej karcie ===
    for i, box in enumerate(card_detection_results.boxes):
        coords = box.xyxy[0].int().tolist()
        x1, y1, x2, y2 = coords

        # === KROK 4: Wycięcie karty z obrazu (bezpośrednio w pamięci) ===
        cropped_card_image = board_image[y1:y2, x1:x2]

        card_class_name = card_detection_results.names[int(box.cls[0])]
        print(f"--- Analizuję kartę nr {i + 1} (wykryty typ: '{card_class_name}') ---")

        # === KROK 5: Przekazanie wyciętego fragmentu do drugiego modelu ===
        sign_detection_results = findSignModel.predict(cropped_card_image)

        # === KROK 6: Zebranie i wyświetlenie wyników dla tej jednej karty ===
        if sign_detection_results.boxes:
            signs = [sign_detection_results.names[int(cls_id)] for cls_id in sign_detection_results.boxes.cls]
            card = CardFactory.create_card(signs)
            # TODO wykryć która strona
            print(sides['left'])
            # sides['left'].append(card)
            print(card)

        else:
            print("  -> Nie znaleziono żadnych symboli na tej karcie.")


if __name__ == "__main__":
    main_pipeline()