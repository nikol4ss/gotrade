from fastapi import FastAPI
from src.router import api_binance_router as binance_routes

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI active"}

app.include_router(binance_routes.router)
