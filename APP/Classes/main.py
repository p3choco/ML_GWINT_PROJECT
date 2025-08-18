from ultralytics import YOLO
import cv2
import numpy as np
from card import Card
from card_factory import CardFactory
from side import Side

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

side = Side(test_cards)

print(side)

# MODEL_PATH = "/Users/piotrbednarski/Desktop/ML_GWINT_PROJECT/znaczki_12s/train/weights/best.pt" 
# model = YOLO(MODEL_PATH)                           

# img_path = "/Users/piotrbednarski/Desktop/ML_GWINT_PROJECT/data/images/aedaec00-brygada_impera.jpg"
# #2aeb2563-trzaskajacy_mroz1
# results = model.predict(source=img_path, conf=0.25, iou=0.7, imgsz=640)

# r = results[0]

# signs = [r.names[cls_id] for cls_id in r.boxes.cls.int().tolist()]
# print(f"LOOK: {signs}")

# card = CardFactory.create_card(test_data[0][0])
# print(card)

