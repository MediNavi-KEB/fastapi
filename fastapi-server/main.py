from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.user_route import user_router
from routes.favorite_routes import router as favorite_router
import uvicorn

# 출처 등록 (CORS)
origins = ["*"]

app = FastAPI()
app.include_router(user_router, prefix="/user")
app.include_router(favorite_router, prefix="/favorites")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080, reload=True)
