import folium
from sqlalchemy import create_engine
import pandas as pd
import time

# SQLAlchemy 연결 설정
engine = create_engine("mysql+mysqldb://root:tiger@localhost/db_test")

# 쿼리 실행 및 결과를 데이터프레임으로 가져오기
query = "SELECT gps_y, gps_x FROM cctv_info"
cctv_data = pd.read_sql_query(query, engine)

# 초기 지도 중심 좌표 설정
initial_lat = float(cctv_data['gps_y'][0])
initial_lon = float(cctv_data['gps_x'][0])
center = [initial_lat, initial_lon]

# Folium 맵 생성
m = folium.Map(location=center, zoom_start=12.5)

# 마커 위치 리스트 생성
loc = []
for index, row in cctv_data.iterrows():
    lon = row['gps_x']
    lat = row['gps_y']
    loc.append([lat, lon])

# 지도에 마커 찍기
for i in range(len(loc)):
    folium.Marker(loc[i], icon=folium.Icon(color='blue', icon='fa-film', prefix='fa')).add_to(m)

# Folium 맵을 HTML 문자열로 변환
maps = m._repr_html_()

# HTML 예시 코드 생성
html_code = f"""
     <div id="map-container">{maps}</div>
"""

# HTML 파일 저장
with open('map.html', 'w') as f:
    f.write(html_code)

#타임슬립
interval = 60  # 작업을 수행할 간격(초)
iterations = 10  # 총 작업 횟수

time.sleep(interval)
