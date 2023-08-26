import requests
import cv2
import os
import json
from private import url

def send_server(results_df, camera_name, frame):
    for i in range(len(results_df)):
        if results_df['action_detection'][i] == 1:
            # Set image path & name
            img_path = f"captured_img/{camera_name}_{results_df['Time'][i]}.jpg"
            # Save image
            cv2.imwrite(img_path, frame)
            
            # POST 요청에 보낼 데이터
            record_data = {
                "cctv_id": camera_name,
                "event_item": results_df['Class_Name'][i],
                "event_time": results_df['Time'][i],
                "event_type": results_df['event_type'][i],
                "event_description": results_df['action_category'][i]
            }
            
            # 데이터 구성
            data = {
                'cctv_data': (None, json.dumps(record_data), 'application/json'),
                'photo': (img_path, open(img_path, 'rb'))
            }
            
            response = requests.post(url, files=data)
            # 응답 확인
            if response.status_code == 200:
                print("Record added successfully.")
            else:
                print("Failed to add record.")
                print(response.status_code)
                print(response.text)
                
            # Delete image
            os.remove(img_path)