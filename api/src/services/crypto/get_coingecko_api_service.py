import os
import sys
import requests
from fastapi import APIRouter

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.script import format_money, format_porcent

router = APIRouter()
url = "https://api.coingecko.com/api/v3/global"

def get_coingecko_api_overview():
    url = "https://api.coingecko.com/api/v3/global"
    response = requests.get(url)
    data = response.json()

    market_cap = data["data"]["total_market_cap"]["usd"]
    volume_24h = data["data"]["total_volume"]["usd"]
    btc_dominance = data["data"]["market_cap_percentage"]["btc"]
    eth_dominance = data["data"]["market_cap_percentage"]["eth"]

    return {
        "market_cap": format_money(market_cap),
        "volume_24h": format_money(volume_24h),
        "btc_dominance": format_porcent(btc_dominance),
        "eth_dominance": format_porcent(eth_dominance)
    }


