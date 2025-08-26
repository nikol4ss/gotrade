export const endpoint = "http://127.0.0.1:8000"

export interface CoinQuotationModel {
  rank: string;
  display_name: string;
  price: string;
  market_cap: string;
  market_cap_rank: number;
  volume: string;
  price_change_24h: string;
  price_change_percentage_24h: string;
  high_24h: string;
  low_24h: string;
  circulating_supply: string;
}
