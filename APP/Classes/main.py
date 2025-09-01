from ultralytics import YOLO
import cv2
import numpy as np
from card import Card
from card_factory import CardFactory
from side import Side
from const.models import FIND_SIGN_MODEL_PATH, FIND_CARDS_MODEL_PATH
from models.find_sign_model import FindSignModel
from models.find_cards_model import FindCardsModel
from const.imgs import PLANSZA1, PLANSZA2, PLANSZA3

test_data = {
    "sword_row": [
        ['2', 'miecz', 'rog'],
        ['5', 'miecz']
    ], 
    "bow_row": [
        ['4', 'lucznik']
    ],
    "catapult_row": [
        ['1', 'katapulta', 'medyk'],
        ['8', 'katapulta', 'wiez']
    ],
    "no_row":  [
        ['foltest zdobywca']
    ]
}


test_cards = {
    row: [CardFactory.create_card(card) for card in cards]
    for row, cards in test_data.items()
}

img_path = "D:\pliki\Studia\kolo\ML_GWINT_PROJECT/data/images/aedaec00-brygada_impera.jpg"
#2aeb2563-trzaskajacy_mroz1
# results = model.predict(source=img_path, conf=0.25, iou=0.7, imgsz=640)



def main():

    findCardsModel = FindCardsModel(FIND_CARDS_MODEL_PATH)
    result = findCardsModel.predict(PLANSZA1)
    class_names = result.names
    if result.boxes:
        for box in result.boxes:
            class_id = int(box.cls[0])
            class_name = class_names[class_id]

            confidence = float(box.conf[0])

            bounding_box = box.xyxy[0].tolist()

            print(f"Obiekt: {class_name}")
            print(f"  Pewność: {confidence:.2f}")
            print(f"  Współrzędne [x1, y1, x2, y2]: {bounding_box}")
            print("-" * 20)
    else:
        print("Nie wykryto żadnych obiektów na obrazie.")
    # findSignModel = FindSignModel(FIND_SIGN_MODEL_PATH)
    # r = findSignModel.predict(img_path)
    #
    # # print(r)
    # signs = [r.names[cls_id] for cls_id in r.boxes.cls.int().tolist()]
    # # print(f"LOOK: {signs}")


main()

