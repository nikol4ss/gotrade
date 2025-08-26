import os
import logging
import requests
from dotenv import load_dotenv

from fastapi import APIRouter
from src.utils.format import format_money, format_porcent, format_number_short, format_dollar_invert

load_dotenv()
router = APIRouter()
logging.basicConfig(level=logging.ERROR)

API_KEY = os.getenv("COINGECKO_API_KEY")
URL = "https://api.coingecko.com/api/v3/"


def get_api_overview():
    url_overview = f"{URL}global"
    headers = {"X-CoinGecko-Api-Key": API_KEY}

    try:
        response = requests.get(url_overview, headers=headers)
        response.raise_for_status()
        data = response.json()

        marketcap = data["data"]["total_market_cap"]["usd"]
        volume = data["data"]["total_volume"]["usd"]
        btc_dom = data["data"]["market_cap_percentage"]["btc"]
        eth_dom = data["data"]["market_cap_percentage"]["eth"]

        return {
            "marketcap": format_money(marketcap),
            "volume": format_money(volume),
            "btc_dom": format_porcent(btc_dom),
            "eth_dom": format_porcent(eth_dom),
        }

    except requests.exceptions.RequestException as error:
        logging.error("Error in request: %s", error)
        data = None


def get_api_topcoins(limit=10, currency="usd"):
    url_topcoins = f"{URL}coins/markets"
    headers = {"X-CoinGecko-Api-Key": API_KEY}
    params = {
        "vs_currency": currency,
        "order": "market_cap_desc",
        "per_page": limit,
        "page": 1,
        "sparkline": False,
        "price_change_percentage": "1h,24h,7d",
    }

    try:
        response = requests.get(url_topcoins, params=params, headers=headers)
        response.raise_for_status()
        coins = response.json()
        result = []

        for coin in coins:
            result.append(
                {
                    "name": coin["name"],
                    "symbol": coin["symbol"].upper(),
                    "price": f"${coin['current_price']:,.2f}",
                    "volume": format_number_short(coin["total_volume"]),
                    "display_name": f"{coin['symbol'].upper()} - {coin['name']}",
                    "market_cap": format_number_short(coin["market_cap"]),
                    "market_cap_rank": coin["market_cap_rank"],
                    "price_change_24h": format_dollar_invert(f"${coin['price_change_24h']:,.2f}"),
                    "price_change_percentage_24h": f"{coin['price_change_percentage_24h']:.2f}%",
                    "high_24h": f"${coin['high_24h']:,.2f}",
                    "low_24h": f"${coin['low_24h']:,.2f}",
                    "circulating_supply": format_number_short(
                        coin["circulating_supply"]
                    ),
                    "logo": coin["image"],
                }
            )

        return result

    except requests.exceptions.RequestException as error:
        logging.error("Error in request: %s", error)
        return None


# def get_market_chart(coin_id, days=30, vs_currency="usd"):
#     """Histórico de preço, market cap e volume"""
#     url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
#     params = {"vs_currency": vs_currency, "days": days}
#     res = requests.get(url, params=params)
#     res.raise_for_status()
#     return res.json()  # retorna prices, market_caps, total_volumes


# def get_crypto_sectors():
#     """Categorias / setores de criptos"""
#     url = "https://api.coingecko.com/api/v3/coins/categories"
#     res = requests.get(url)
#     res.raise_for_status()
#     categories = res.json()
#     result = []
#     for cat in categories:
#         result.append(
#             {
#                 "id": cat["id"],
#                 "name": cat["name"],
#                 "market_cap": cat["market_cap"],
#                 "volume_24h": cat["volume_24h"],
#                 "market_cap_change_24h": cat.get("market_cap_change_24h"),
#             }
#         )
#     return result


# def get_total_cryptos():
#     """Número total de criptos ativas"""
#     url = "https://api.coingecko.com/api/v3/coins/list"
#     res = requests.get(url)
#     res.raise_for_status()
#     coins = res.json()
#     return len(coins)
