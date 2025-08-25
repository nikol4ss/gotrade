import os
import sys
from fastapi import APIRouter

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.crypto.get_coingecko_api_service import get_coingecko_api_overview

router = APIRouter()


@router.get("/api/coingecko")
def get_api_coingecko():
    return get_coingecko_api_overview()

