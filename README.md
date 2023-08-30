<div align= "center">
    <img src="https://capsule-render.vercel.app/api?type=waving&color=auto&height=180&text=是是非非&animation=&fontColor=ffffff&fontSize=70" />
    </div>

<h1 style="border-bottom: 1px solid #d8dee4; color: #282d33; font-size: 25px"> 📖 Project</h1>

### ■ Description
#### 🚘 종합 기능형 교통 관제 시스템 🚘

### ■ Software Used
> [🚀 YOLOv5](https://github.com/ultralytics/yolov5): Object Detection

> OpenCV: Live Image Capture

> Pytorch: YOLOv5 Model Learning

### ■ Service Framework

<img src = "https://github.com/SCUTUM98/KFQ_TEAM01/assets/43438476/95e37c72-3778-4e37-a128-6d739889b76a">

### ■ Image Segmentation

### ■ YOLO Object Detection
#### 🚀 상황 판단 로직의 결과와 모델 학습에 사용된 데이터셋의 출처는 [YOLO INFO](https://github.com/SCUTUM98/KFQ_TEAM01/blob/main/yolo/README.md)를 참고하세요.

#### 🚀 YOLO Framework

<img src = "https://github.com/SCUTUM98/KFQ_TEAM01/assets/43438476/d9b043e5-9586-4539-b999-0fe419d51ca8">

#### 🚀 Road Boundary Check

#### 🚀 Object Detection
##### 📹 YOLOv5m
##### - Class: 80
##### - Used Class: Person, Bicycle, Motorcycle, Car, Bus, Truck

<div align = "center">
<img src = "https://github.com/SCUTUM98/KFQ_TEAM01/assets/43438476/3932020b-731c-48a8-9c46-00af9ae064bd" style="width: 600px; height: auto;">
<img src = "https://github.com/SCUTUM98/KFQ_TEAM01/assets/43438476/90c634e9-c9b2-4c6a-a8b7-8ef772be0f13" style="width: 600px; height: auto;"></div>

##### 🐶 Animal Detection Model
##### - Class: 5
##### - Used Class: Cat, Dog, Deer/Elk, Racoon, Wild boar/Pig

<img src = "https://github.com/SCUTUM98/KFQ_TEAM01/assets/43438476/d94db4f4-79c4-4b46-b5bd-d083d72f2ec1" style="width: 600px; height: auto;">

##### 🔥 Fire Detection Model
##### - Class: 3
##### - Used Class: Fire, Smoke, Car fire

<img src = "https://github.com/SCUTUM98/KFQ_TEAM01/assets/43438476/d8b3c480-d433-4126-b328-59a2aaf7074d" style="width: 600px; height: auto;">

##### 📦 Obstacle Detection Model
##### - Class: 5
##### - Used Class: Tree, Box, Tire, Drum can, Rock

<img src = "https://github.com/SCUTUM98/KFQ_TEAM01/assets/43438476/82813a9a-4a03-47f2-b75c-760e1e7150f5" style="width: 600px; height: auto;">

### ■ API Service
```treebash
FastAPI/ : 패키지/모듈 root.
│
├── model/ : API로 주고받을 데이터 model 정의.
│   ├── cctv_model.py : cctv 등록/조회 관련 API 입력 param 및 응답 데이터에 대한 model.
│   └── ...
│
├── repository/ : mysql db CRUD 관련 로직 및 데이터 model 정의.
│   ├── cctv_repo.py : cctv 테이블에 대한 CRUD 처리 및 cctv 테이블 데이터 model 구현.
│   └── ...
│
├── resource/ : API server 동작에 필요한 각종 시스템 리소스(database 접속 등).
│   ├── database.py : DB 접속 및 session 연결 관련 코드.
│   └── ...
│
├── router/ : API endpoint별 처리 로직.
│   ├── cctv.py : cctv 등록, 조회 관련 API 경로 및 대응되는 endpoint 로직 구현.
│   └── ...
│
├── main.py : API server를 실행할 main 파일.
└── Vehicle/
    └── ...

```

### ■ WEB

```treebash
FastAPI/
│
├── static/ : 웹 애플리케이션에서 변하지 않는 파일
│   ├── events_map.py : 실시간으로 데이터베이스에서 정보를 불러와 이벤트 지도 생성 파일
│   ├── events_list.py : 지도에 나타나는 정보를 보여주는 파일
│   ├── pie_graph.py : 실시간 데이터에 따른 그래프 생성 파일
│   ├── line_graph.py
│   ├── info_table.py
│   ├── event_table.py
│   ├── css  
│   ├── img  
│   ├── js  
│   ├── vendor
│   └── ...
│
└── templates/ : 동적 데이터를 HTML에 삽입하여 동적 웹 페이지를 생성하는 데 사용되는 파일
│   ├── base.html : 페이지에서 기본 틀이 되는 부분
│   ├── home.html : 메인 페이지
│   ├── intro.html
│   ├── charts.html
│   ├── table.html
│   └── ...
└── Vehicle/..
```

<h1 style="border-bottom: 1px solid #d8dee4; color: #282d33; font-size: 25px"> 🪪 Mentor </h1>

#### 💻 CheolWoo Kim

<h1 style="border-bottom: 1px solid #d8dee4; color: #282d33; font-size: 25px"> 🪪 Crew </h1> 

#### 💻 HyoSang Yoo(Team Leader, API Server, Statistics Visualization)

<div align = "center">
    <img src = "https://github.com/SCUTUM98/KFQ_TEAM01/assets/43438476/14b9fd5d-4531-4eb7-bce4-ad686dcb078d" 
    style="width:100px; height:200px;"></div>
    <div  align= "center"><img src="https://img.shields.io/badge/C-A8B9CC?style=flat-square&logo=C&logoColor=white">
    <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white">
    <img src="https://img.shields.io/badge/Notion-000000?style=flat-square&logo=Notion&logoColor=white">
    <img src="https://img.shields.io/badge/C++-00599C?style=flat-square&logo=C%2B%2B&logoColor=white">
    <img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=MySQL&logoColor=white"></div>

#### 💻 BonGeun Gu(YOLO Model, Detection Logic, Object Detection, OpenCV)

<div align = "center">
    <img src = "https://github.com/SCUTUM98/KFQ_TEAM01/assets/43438476/7c2e9311-b970-4542-b830-2232c8154b9d" 
    style="width:100px; height:200px;"></div>
    <div  align = "center"> 
    <img src="https://img.shields.io/badge/C-A8B9CC?style=flat-square&logo=C&logoColor=white">
    <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white">
    <img src="https://img.shields.io/badge/Notion-000000?style=flat-square&logo=Notion&logoColor=white">
    <img src="https://img.shields.io/badge/Amazon S3-569A31?style=flat-square&logo=Amazon S3&logoColor=white">
    <img src="https://img.shields.io/badge/Android-3DDC84?style=flat-square&logo=Android&logoColor=white">
    <br/><img src="https://img.shields.io/badge/Amazon AWS-232F3E?style=flat-square&logo=Amazon AWS&logoColor=white">
    <img src="https://img.shields.io/badge/C++-00599C?style=flat-square&logo=C%2B%2B&logoColor=white">
    <img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=MySQL&logoColor=white">
    <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=HTML5&logoColor=white">
    <img src="https://img.shields.io/badge/Javascript-F7DF1E?style=flat-square&logo=Javascript&logoColor=white">
    <img src="https://img.shields.io/badge/Java-007396?style=flat-square&logo=Java&logoColor=white"></div>

#### 💻 Gwangwon Lee(Image Segementation)

<div align = "center">
    <img src = "https://github.com/SCUTUM98/KFQ_TEAM01/assets/43438476/94ca4c18-736e-4533-a444-ac44b1baa0a4" 
    style="width:100px; height:200px;"></div>
    <div  align = "center">  
    <div  align= "center"><img src="https://img.shields.io/badge/C-A8B9CC?style=flat-square&logo=C&logoColor=white">
    <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white">
    <img src="https://img.shields.io/badge/Notion-000000?style=flat-square&logo=Notion&logoColor=white">
    <img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=MySQL&logoColor=white">
    <img src="https://img.shields.io/badge/Java-007396?style=flat-square&logo=Java&logoColor=white"></div>
</div>

#### 💻 YeLin Lee(API Server, WEB Service)

<div align = "center">
    <img src = "https://github.com/SCUTUM98/KFQ_TEAM01/assets/43438476/b4e74df5-d007-4d9e-863f-f6f214c58b4e" 
    style="width:100px; height:200px;"></div>
    <div  align= "center"><img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white">
    <img src="https://img.shields.io/badge/Notion-000000?style=flat-square&logo=Notion&logoColor=white">
    <img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=MySQL&logoColor=white">
    <img src="https://img.shields.io/badge/Matlab-0076a8?style=flat-square&logo=Matlab&logoColor=white">
<img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=HTML5&logoColor=white"></div>
</div>

#### 💻 Doyeon Park(DB, Statistics & Map Visualization)

<div align = "center">
    <img src = "https://github.com/SCUTUM98/KFQ_TEAM01/assets/43438476/93095210-be99-4bf3-8a24-690081c6cfdd" 
    style="width:100px; height:200px;"></div>
    <div  align= "center"><img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white">
    <img src="https://img.shields.io/badge/Notion-000000?style=flat-square&logo=Notion&logoColor=white">
    <img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=MySQL&logoColor=white">
    <img src="https://img.shields.io/badge/Slack-4A154B?style=flat-square&logo=Slack&logoColor=white">
<img src="https://img.shields.io/badge/Amazon AWS-232F3E?style=flat-square&logo=Amazon AWS&logoColor=white"></br>
<img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=Docker&logoColor=white"></div>

<h1 style="border-bottom: 1px solid #d8dee4; color: #282d33;"> 🧑‍💻 Contact us </h1> <br> 
    <div align= "center">  </div>  <br> 
    <div align= "center"> <a href="https://hits.seeyoufarm.com"> <img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FKFQ Final Project%2F&count_bg=%23000000&title_bg=%23000000&icon=github.svg&icon_color=%23FFFFFF&title=GitHub&edge_flat=false"/></a>
       </div> 
    </div>
    <div style="text-align: left;"> 
    <h1 style="border-bottom: 1px solid #d8dee4; color: #282d33;"> 🏅 Stats </h1> <div align= "center"> <img src="https://github-readme-stats.vercel.app/api?username=KFQ Final Project&bg_color=180,00000000,&title_color=000000&text_color=000000"
         /> <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=KFQ Final Project&layout=compact&bg_color=180,00000000,&title_color=000000&text_color=000000"
           /> </div> 
    </div>