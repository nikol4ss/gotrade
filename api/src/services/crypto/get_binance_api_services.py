import os
import sys
import locale

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from binance_api_services import connect_api_binance

client = connect_api_binance()
locale.setlocale(locale.LC_ALL, "en_US.UTF-8")

if client:
    ticket = client.get_ticker()

    def get_top_coins():
        usdt = [c for c in ticket if c["symbol"].endswith("USDT")] # type: ignore

        volume = sorted(usdt, key=lambda x: float(x["quoteVolume"]), reverse=True)[:10]
        order_coin = sorted(volume, key=lambda x: float(x["lastPrice"]), reverse=True)

        list_coin = [
            f"{coin['symbol'].replace('USDT','')} - {locale.currency(float(coin['lastPrice']), grouping=True)}"
            for coin in order_coin
        ]

        for coin in list_coin:
            print(coin)

        return list_coin


get_top_coins()
