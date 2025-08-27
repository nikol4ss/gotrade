import os
import time
import logging
import requests
from fastapi import APIRouter
from dotenv import load_dotenv

from src.utils.format import (
    format_money,
    format_porcent,
    format_number_short,
    format_dollar_invert,
)

load_dotenv()
router = APIRouter()
logging.basicConfig(level=logging.ERROR)

API_KEY = os.getenv("COINGECKO_API_KEY")
API_URL = os.getenv("COINGECKO_API_URL")


def get_api_overview(retries: int = 3, delay: float = 2.0) -> dict[str, str] | None:
    """Get global cryptocurrency market data from CoinGecko.

    Parameters:
        retries (int): Number of retry attempts if request fails (default 3).
        delay (float): Seconds to wait between retries (default 2.0).

    Returns:
        dict[str, str]: Market overview with formatted strings:
            - marketcap: Total market cap (e.g., '$1,234,567.89')
            - volume: Total 24h volume (e.g., '$234,567.89')
            - btc_dom: BTC dominance percentage (e.g., '%45.67')
            - eth_dom: ETH dominance percentage (e.g., '%13.13')
        None: If all attempts fail.
    """
    url_overview = f"{API_URL}global"
    headers = {"X-CoinGecko-Api-Key": API_KEY}

    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url_overview, headers=headers, timeout=10)
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
            logging.error(
                "Attempt %d/%d failed: %s (URL: %s)",
                attempt,
                retries,
                error,
                url_overview,
            )
            if attempt < retries:
                time.sleep(delay)
            else:
                return None


def get_api_topcoins(
    limit: int = 10, currency: str = "usd", retries: int = 3, delay: float = 2.0
) -> list[dict[str, str]] | None:
    """Fetch top cryptocurrencies by market capitalization from CoinGecko.

    Parameters:
        limit (int): Number of top coins to retrieve (default 10).
        currency (str): Currency to display prices in (default 'usd').
        retries (int): Number of retry attempts if request fails (default 3).
        delay (float): Seconds to wait between retry attempts (default 2.0).

    Returns:
        list[dict[str, str]]: List of top coins with formatted data:
            - name: Coin name (e.g., 'Bitcoin')
            - logo: Coin image URL
            - symbol: Coin symbol (uppercase)
            - display_name: Symbol and name combined (e.g., 'BTC - Bitcoin')
            - price: Current price (e.g., '$34,567.89')
            - market_cap: Market capitalization (e.g., '$1.23B')
            - volume: 24h trading volume (e.g., '$234.56M')
            - market_cap_rank: Rank by market cap
            - price_change_percentage_24h: 24h % change (e.g., '%1.23')
            - price_change_24h: 24h absolute change (e.g., '$-123.45')
            - high_24h: Highest price in 24h
            - low_24h: Lowest price in 24h
            - circulating_supply: Coins in circulation (e.g., '18.7M')
        None: If request fails after all retries.
    """
    url_topcoins = f"{API_URL}coins/markets"
    headers = {"X-CoinGecko-Api-Key": API_KEY}
    params = {
        "vs_currency": currency,
        "order": "market_cap_desc",
        "per_page": limit,
        "page": 1,
        "sparkline": False,
        "price_change_percentage": "1h,24h,7d",
    }

    for attempt in range(1, retries + 1):
        try:
            response = requests.get(
                url_topcoins, params=params, headers=headers, timeout=10
            )
            response.raise_for_status()
            coins = response.json()
            result = []

            for coin in coins:
                result.append(
                    {
                        "name": coin["name"],
                        "logo": coin["image"],
                        "symbol": coin["symbol"].upper(),
                        "display_name": f"{coin['symbol'].upper()} - {coin['name']}",
                        "price": format_money(coin["current_price"]),
                        "market_cap": format_number_short(coin["market_cap"]),
                        "volume": format_number_short(coin["total_volume"]),
                        "market_cap_rank": coin["market_cap_rank"],
                        "price_change_percentage_24h": format_porcent(
                            coin["price_change_percentage_24h"]
                        ),
                        "price_change_24h": format_dollar_invert(
                            format_money(coin["price_change_24h"])
                        ),
                        "high_24h": format_money(coin["high_24h"]),
                        "low_24h": format_money(coin["low_24h"]),
                        "circulating_supply": format_number_short(
                            coin["circulating_supply"]
                        ),
                    }
                )

            return result

        except requests.exceptions.RequestException as error:
            logging.error(
                "Attempt %d/%d failed: %s (URL: %s)",
                attempt,
                retries,
                error,
                url_topcoins,
            )
            if attempt < retries:
                time.sleep(delay)
            else:
                return None


def get_api_market_chart(coin_id, days=30, currency="usd"):
    url = f"{API_URL}coins/{coin_id}/market_chart"
    params = {"vs_currency": currency, "days": days}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as error:
        logging.error("Error in request: %s", error)
        return None


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
