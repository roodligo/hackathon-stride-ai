from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO('models/yolov8m.pt')  # use o medium em vez do nano

    model.train(
        data='dataset/images/data.yaml',
        epochs=150,  # mais treino se o dataset for pequeno
        imgsz=960,   # aumentar resolução
        batch=4,     # reduzir se estiver com pouco VRAM
        workers=2,
        patience=30  # parar cedo se não melhorar
    )
