from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def 이름():
  return '보낼 값'

@app.get("/two")
def car():
  import pandas as pd
  import os
  import glob
#파일경로는 개인별로 바꿔주세요
  folder_path = r'C:/work/python/python_basic/KFQ_TEAM01-1/yolo/results/xlsxdata'
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


  