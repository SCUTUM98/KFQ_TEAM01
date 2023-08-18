# 1. EVENT_TYPE
```treebash
EVENT/ : YOLO Object Detection을 통해 인지되는 Object를 기반으로 Event_type을 지정
│
├── Human/
│   ├── P01 : person detected
│   └── ...
│
├── Bicycle or Motorcycle/
│   ├── B01 : bicycle detected with person
│   ├── B02 : motorcycle detected with person
│   └── ...
│
├── Fire/
│   ├── F01 : fire detected
│   ├── F02 : smoke detected
│   ├── F03 : car fire detected
│   └── ...
│
├── Animal/
│   ├── A01 : cat or dog detected
│   ├── A02 : deer or elk detected
│   ├── A03 : racoon detected
│   └── A04 : wild boar or pig detected
│
└── Obstacle/
    └── ...
```

# 2. Used Dataset
## 2.1. yolo5m
* https://github.com/ultralytics/yolov5

## 2.2 Fire detection
### Roboflow
* https://universe.roboflow.com/porvip/fire-szxx8
### Other Dataset
* 아래 내용은 대충 적은거라 정확히 해보고 수정 필요.

## 2.3 Animals detection
### Roboflow
* cat: 
* deer:
* dog:
* racoon:
* wild boar: 