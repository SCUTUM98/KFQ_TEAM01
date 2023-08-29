from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from router.cctv_router import cctv_router
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# 원래는 보안상 이렇게 하면 안됨
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# html파일이 있는 static폴더로 경로 설정
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(cctv_router, prefix="/cctv")


@app.get("/")
async def home(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("home.html", context)


@app.get("/intro1")
async def intro1(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("intro1.html", context)


@app.get("/intro2")
async def intro2(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("intro2.html", context)


@app.get("/charts")
async def charts(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("charts.html", context)


@app.get("/table1")
async def table1(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("table1.html", context)


@app.get("/table2")
async def table2(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("table2.html", context)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)



