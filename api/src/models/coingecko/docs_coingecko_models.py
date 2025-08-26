from pydantic import BaseModel


class CoinGeckoOverviewModel(BaseModel):
    marketcap: str
    volume: str
    btc_dom: str
    eth_dom: str


class TopCoinModel(BaseModel):
    name: str
    symbol: str
    display_name: str
    price: str
    volume: str
    market_cap: str
    market_cap_rank: int
    price_change_24h: str
    price_change_percentage_24h: str
    high_24h: str
    low_24h: str
    circulating_supply: str
