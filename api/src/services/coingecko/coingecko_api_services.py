import logging
import requests

from fastapi import APIRouter
from src.utils.script import format_money, format_porcent

router = APIRouter()
logging.basicConfig(level=logging.ERROR)


def get_api_overview():
    url_overview = "https://api.coingecko.com/api/v3/global"

    try:
        response = requests.get(url_overview)
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
    url_topcoins = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": currency,
        "order": "market_cap_desc",
        "per_page": limit,
        "page": 1,
        "sparkline": False,
        "price_change_percentage": "1h,24h,7d",
    }

    try:
        response = requests.get(url_topcoins, params=params)
        response.raise_for_status()
        coins = response.json()
        result = []

        for coin in coins:
            result.append(
                {
                    "name": coin["name"],
                    "symbol": coin["symbol"].upper(),
                    "current_price": coin["current_price"],
                    "marketcap": coin["market_cap"],
                    "marketcap_rank": coin["market_cap_rank"],
                    "volume": coin["total_volume"],
                    "circulating": coin.get("circulating_supply"),
                    "price_change_24h": coin.get("price_change_percentage_24h"),
                }
            )

        return result

    except requests.exceptions.RequestException as error:
        logging.error("Error in request: %s", error)
        result = None


def get_market_chart(coin_id, days=30, vs_currency="usd"):
    """Histórico de preço, market cap e volume"""
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {"vs_currency": vs_currency, "days": days}
    res = requests.get(url, params=params)
    res.raise_for_status()
    return res.json()  # retorna prices, market_caps, total_volumes

def get_crypto_sectors():
    """Categorias / setores de criptos"""
    url = "https://api.coingecko.com/api/v3/coins/categories"
    res = requests.get(url)
    res.raise_for_status()
    categories = res.json()
    result = []
    for cat in categories:
        result.append({
            "id": cat["id"],
            "name": cat["name"],
            "market_cap": cat["market_cap"],
            "volume_24h": cat["volume_24h"],
            "market_cap_change_24h": cat.get("market_cap_change_24h")
        })
    return result

def get_total_cryptos():
    """Número total de criptos ativas"""
    url = "https://api.coingecko.com/api/v3/coins/list"
    res = requests.get(url)
    res.raise_for_status()
    coins = res.json()
    return len(coins)
