import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.script import format_money, map_selector
from binance_api_services import connect_api_binance

client = connect_api_binance()

if client:
    ticket = client.get_ticker()

    def get_top_coins():
        usdt = [c for c in ticket if c["symbol"].endswith("USDT")]

        top_volume = sorted(usdt, key=lambda x: float(x["quoteVolume"]), reverse=True)[
            :10
        ]

        top_ordered = sorted(
            top_volume, key=lambda x: float(x["lastPrice"]), reverse=True
        )

        return [
            {
                "crypto": coin["symbol"].replace("USDT", ""),
                "symbol": coin["symbol"],
                "price": format_money(round(float(coin["lastPrice"]), 2)),
                "volume": format_money(round(float(coin["quoteVolume"]), 2)),
            }
            for coin in top_ordered
        ]

    def get_crypto_sectors():
        usdt = [c for c in ticket if c["symbol"].endswith("USDT")]
        volume = sorted(usdt, key=lambda x: float(x['quoteVolume']), reverse=True)[:10]

        sector_volume = {}

        for t in volume:
            symbol = t['symbol'].replace('USDT', '')
            setor = map_selector(symbol)
            volume = float(t['quoteVolume'])
            sector_volume[setor] = sector_volume.get(setor, 0) + volume

        return sector_volume
