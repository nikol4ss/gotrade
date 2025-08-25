import os
import sys
import requests
from fastapi import APIRouter

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.script import format_money

router = APIRouter()
url = "https://api.coingecko.com/api/v3/global"

def get_market_cap():
    response = requests.get(url)
    data = response.json()

    total = 0

    for coin in data:
        market_cap = data["data"]["total_market_cap"]["usd"]
        total += market_cap

    formated_total = format_money(total)
    return formated_total

def get_trading_volume():
    url = "https://api.coingecko.com/api/v3/global"
    response = requests.get(url)
    data = response.json()

    volume_24h = data["data"]["total_volume"]["usd"]

    formated_total = format_money(volume_24h)
    return formated_total

