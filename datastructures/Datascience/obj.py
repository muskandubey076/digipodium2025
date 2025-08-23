from ultralytics import YOLO
# pre - trained YOLOv8 Name model (fast aur lightweight)
modle = YOLO("yolov8n.pt")
#webcam se live object detection (sourece=0 matlab default camera)
modle.predict(
    source=0,#wwebcam
    show=True,#live window dikhayyenge
    conf=0.5#confidence threshold(50%)
)
#pip install -U ultralytics
#pip install torch==2.4.1 torchvision==0.19.1
#to run :open terminal and type python filename.py