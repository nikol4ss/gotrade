from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.router.api_coingecko_router import router as coingecko_routes

app = FastAPI()

CORS_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "FastAPI active"}


app.include_router(coingecko_routes)
