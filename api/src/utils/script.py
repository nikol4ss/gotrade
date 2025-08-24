def format_money(value: float) -> str:
    return f"${value:,.2f}"

def map_selector(symbol):
    symbol = symbol.upper()

    if symbol in ["BTC", "LTC", "BCH", "DOGE"]:
        return "Store of Value / Payment"
    if symbol in ["ETH", "SOL", "ADA", "AVAX", "BNB"]:
        return "Smart Contracts"
    if symbol in ["USDT", "USDC", "DAI", "BUSD"]:
        return "Stablecoins"
    if symbol in ["UNI", "AAVE", "MKR"]:
        return "DeFi"
    if symbol in ["MATIC", "OP", "ARB"]:
        return "Infrastructure / L2"
    return "Others"


# import requests

# url = "https://api.coingecko.com/api/v3/coins/markets"
# params = {
#     "vs_currency": "usd",
#     "order": "market_cap_desc",
#     "per_page": 10,
#     "page": 1,
#     "sparkline": False
# }

# response = requests.get(url, params=params)
# top10 = response.json()

# for coin in top10:
#     print(f"{coin['name']} ({coin['symbol'].upper()}): Market Cap = ${coin['market_cap']:,}, Categoria = {coin.get('categories', 'Unknown')}")
