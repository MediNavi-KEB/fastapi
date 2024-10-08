from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.user_route import user_router
from routes.favorite_route import favorite_router
from routes.calendar_route import calendar_router
from routes.news_route import news_router
from routes.disease_route import disease_router
import uvicorn
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 출처 등록 (CORS)
origins = ["*"]

app = FastAPI()

app.include_router(user_router, prefix="/user")
app.include_router(favorite_router, prefix="/favorite", )
app.include_router(disease_router, prefix="/disease")
app.include_router(calendar_router, prefix="/calendar")
app.include_router(news_router, prefix="/news")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# python main.py로 실행
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
