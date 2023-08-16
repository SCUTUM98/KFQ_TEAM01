import cv2
import time
import datetime

def capture_and_process(cap):
    ret, frame = cap.read()  # 프레임 읽기
    if ret:
        # 현재 시간을 가져와 이미지가 찍힌 시간 저장
        capture_time = datetime.datetime.now()
        
        return frame, capture_time
    else:
        print("Error: No frame detected")
        return None, None
