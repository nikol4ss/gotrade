import os
import sys
from fastapi import APIRouter

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from services.binance_api_services import connect_api_binance
from services.crypto.get_binance_api_services import get_top_coins, get_crypto_sectors

router = APIRouter()
client = connect_api_binance()

if client:
    @router.get("/api/binance/top-coins")
    def get_api_coin():
        return get_top_coins()

    @router.get("/api/binance/crypto-sectors")
    def get_api_crypto_sectors():
        return get_crypto_sectors()
