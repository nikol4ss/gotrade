import os
from dotenv import load_dotenv

from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_SECRET_KEY")


def connect_api_binance(api_key=API_KEY, api_secret=API_SECRET):

    if not api_key or not api_secret:
        print(
            "API key or secret is missing. Please set them in the environment variables."
        )
        return None

    try:
        client = Client(api_key, api_secret)
        print(client.ping())
        client.get_account()
        return client

    except (BinanceAPIException, BinanceOrderException) as error:
        print(f"Error connecting to Binance API: {error}")
        return None
