export interface CoinGeckoOverview {
  marketcap: string
  volume: string
  btc_dom: string
  eth_dom: string
}

export interface CoinGeckoCoin {
  name: string;
  symbol: string;
  display_name: string;
  logo: string;
  price: string;
  price_change_24h: string;
  price_change_percentage_24h: string;
  high_24h: string;
  low_24h: string;
  market_cap: string;
  market_cap_rank: number;
  volume: string;
  circulating_supply: string;
}

export interface CoinGeckoMarketChartPrice {
  date: string;
  price: string;
}

export interface CoinGeckoMarketChart {
  coin_id: string;
  prices: CoinGeckoMarketChartPrice[];
}

export interface DropdownMenuCheckboxItemProps {
  text1: string,
}
