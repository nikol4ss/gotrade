def format_money(value: float) -> str:
    return f"${value:,.2f}"


def format_number_short(n):
    if n >= 1_000_000_000:
        return f"{n/1_000_000_000:.2f}B"
    elif n >= 1_000_000:
        return f"{n/1_000_000:.2f}M"
    elif n >= 1_000:
        return f"{n/1_000:.2f}K"
    else:
        return str(n)


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


def format_porcent(value: float):
    return f"%{value:.2f}"
