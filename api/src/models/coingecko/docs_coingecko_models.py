from pydantic import BaseModel

class CoinGeckoOverviewModel(BaseModel):
    marketcap: str
    volume: str
    btc_dom: str
    eth_dom: str

class TopCoinModel(BaseModel):
    name: str
    symbol: str
    price: str
    volume: str
