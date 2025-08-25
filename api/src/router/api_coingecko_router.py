import os
import sys
from fastapi import APIRouter

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.crypto.get_coingecko_api_service import get_market_cap

router = APIRouter()

@router.get("/api/coingecko/market-cap")
def get_api_market_cap():
    return get_market_cap()
