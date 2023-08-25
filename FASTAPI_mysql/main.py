from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router.cctv_router import user_router
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
import os

app = FastAPI()

# http파일이 있는 static폴더로 경로 설정
app.mount('/static', StaticFiles(directory='static'), name = 'static')

@app.get("/")
def read_root():
    return FileResponse('static/index.html')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


# 원래는 보안상 이렇게 하면 안됨
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router, prefix="/user")