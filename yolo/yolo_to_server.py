import requests
from private import url

def send_server(results_df, camera_name):
    for i in range(len(results_df)):
        if results_df['action_detection'][i] == 1:
            # POST 요청에 보낼 데이터
            record_data = {
                "cctv_id": camera_name,
                "event_item": results_df['Class_Name'][i],
                "event_time": results_df['Time'][i],
                "event_type": results_df['event_type'][i],
                "event_description": results_df['action_category'][i]
            }
            
            print(record_data)
            
            headers = {
                "Content-Type": "application/json"  # Specify the content type
            }

            response = requests.post(url, json=record_data, headers=headers)
            # POST 요청 보내기
            #response = requests.post(f"{url}/cctv/records", json=record_data)

            # 응답 확인
            if response.status_code == 200:
                print("Record added successfully.")
            else:
                print("Failed to add record.")
                print(response.status_code)
                print(response.text)