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
    logo: str
    price: str
    price_change_24h: str
    price_change_percentage_24h: str
    high_24h: str
    low_24h: str
    market_cap: str
    market_cap_rank: int
    volume: str
    circulating_supply: str


class MarketChartModel(BaseModel):
    coin_id: str
    prices: list

