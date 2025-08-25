import os
import sys
import requests
from fastapi import APIRouter

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.script import format_money

router = APIRouter()

def get_market_cap():
        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {
            "vs_currency": "usd",
            "order": "market_cap_desc",
            "per_page": 10,
            "page": 1,
            "sparkline": False,
        }

        response = requests.get(url, params=params)
        data = response.json()

        total = 0
        
        for coin in data:
            mc = coin["market_cap"]
            total += mc

        formated_total = format_money(total)

        return formated_total
