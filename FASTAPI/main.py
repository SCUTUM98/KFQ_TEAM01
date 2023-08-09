from fastapi import FastAPI
import json
import pandas as pd
import os
import glob

app = FastAPI()

@app.get("/")
def name():
  return '보낼 값'

@app.get("/two")
def car():
#파일경로는 개인별로 바꿔주세요
  folder_path = r'/Users/bongeungu/Desktop/kfq/KFQ_TEAM01/yolo/results/xlsxdata'
  excel_files = glob.glob(os.path.join(folder_path, '*.csv'))
  excel_files = [path.replace("\\", "/") for path in excel_files]

  for i, n in enumerate(range(len(excel_files))):
      if i == 0:
          file_name=excel_files[n] 
          df= pd.read_csv(file_name)
          df = df.to_dict('records')
      else:
          file_name=excel_files[n] 
          new_df=pd.read_csv(file_name)
          new_df = new_df.to_dict('records')
          df.append(new_df)
  
  return df
  
  """
  merged_data=[]
  for i, file_name in enumerate(excel_files):
    if i == 0:
        df = pd.read_csv(file_name)
        merged_data.extend(df.to_dict('records'))
    else:
        new_df = pd.read_csv(file_name)
        merged_data.extend(new_df.to_dict('records'))

  # 리스트 형태의 딕셔너리를 JSON으로 변환
  json_data = json.dumps(merged_data)
  
  return json_data
  """
