from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.user_route import user_router

# 출처 등록 (CORS)
origins = ["*"]

app = FastAPI()
app.include_router(user_router, prefix="/user")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)