from ultralytics import YOLO
import torch

class FindCardsModel:
    def __init__(self, model_path):
        self.model = YOLO(model_path)

    def predict(self, img_path: str):
        return self.model.predict(source=img_path, conf=0.25, iou=0.7, imgsz=640)[0]