def format_money(value: float) -> str:
    return f"${value:,.2f}"


def map_selector(symbol):
    symbol = symbol.upper()

    # Store of Value / Payment
    if symbol in ["BTC", "LTC", "BCH", "DOGE"]:
        return "Store of Value / Payment"

    # Smart Contracts
    if symbol in ["ETH", "SOL", "ADA", "AVAX", "BNB"]:
        return "Smart Contracts"

    # Stablecoins
    if symbol in ["USDT", "USDC", "DAI", "BUSD", "FDUSD"]:
        return "Stablecoins"

    # DeFi
    if symbol in ["UNI", "AAVE", "MKR"]:
        return "DeFi"

    # Infrastructure / Layer 2
    if symbol in ["MATIC", "OP", "ARB"]:
        return "Infrastructure / L2"

    # Meme / Community Coins
    if symbol in ["MEME", "SHIB", "DOGE"]:
        return "Meme / Community"

    # Utility / Tokens específicos
    if symbol in ["BIO", "XRP"]:
        return "Utility / Payment Network"

    return "Others"

    # volume_24h = data["data"]["total_volume"]["usd"]
    # btc_dominance = data["data"]["market_cap_percentage"]["btc"]
