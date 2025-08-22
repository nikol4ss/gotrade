import os
import sys
from fastapi import APIRouter

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from services.binance_api_services import connect_api_binance
from services.crypto.get_binance_api_services import get_top_coins

router = APIRouter()
client = connect_api_binance()

if client:
    @router.get("/api/binance/top-coins")
    def get_coin():
        if not client:
            return {"error": "Could not connect to Binance API"}
        return get_top_coins()
