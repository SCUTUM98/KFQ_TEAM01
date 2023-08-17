from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from router.cctv_router import cctv_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(cctv_router, prefix="/cctv")