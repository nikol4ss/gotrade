export const endpoint = "http://127.0.0.1:8000"

export interface CoinQuotationModel {
  display_name: string;
  price: string;
  market_cap: string;
  volume: string;
  price_change_24h: string;
  price_change_percentage_24h: string;
  high_24h: string;
  low_24h: string;
  circulating_supply: string;
}
