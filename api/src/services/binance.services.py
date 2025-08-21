import os
from dotenv import load_dotenv
from binance.client import Client

load_dotenv()

api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_SECRET_KEY")

client = Client(api_key, api_secret)

ticker = client.get_symbol_ticker(symbol="BTCUSDT")
print("Ticker:", ticker)

balance = client.get_asset_balance(asset="BTC")
print("Balance:", balance)

