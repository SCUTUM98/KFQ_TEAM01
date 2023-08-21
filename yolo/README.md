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
├── Obstacle/
│   ├── 
│   ├──
│   ├──
│   ├──
│   ├──
│   └── ...
│
└── Vehicle/
    └── ...
```

# 2. Used Dataset
## 2.1. yolo5m
* https://github.com/ultralytics/yolov5

## 2.2 Fire detection
### Roboflow
* https://universe.roboflow.com/porvip/fire-szxx8
### Other Dataset
* Car fire detection

## 2.3 Animals detection
### Roboflow
* cat: https://universe.roboflow.com/yolo-4akh3/cat-model-oyjob
* deer: https://universe.roboflow.com/jwellstx-ahvez/deerface
* dog: https://universe.roboflow.com/tansam-uunrl/dog-detector1
* racoon: https://universe.roboflow.com/objectdection2/racoonsfinder
* wild boar: https://universe.roboflow.com/workspace1-lhfkr/wildboar-afbbo

## 2.4 Obstacle detection
### Roboflow
* Tree: https://universe.roboflow.com/tree-detection-h9dcy/tree-detection-ekaot
* Rock: https://universe.roboflow.com/iskandar/rock-detection-hhird
* Box: https://universe.roboflow.com/objectdetection-rclje/parceldetection-cdilp
* Tire: https://universe.roboflow.com/robert-almalak/tires-9zgkh
### Other Dataset
* Drum can