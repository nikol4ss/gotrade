export interface Coin {
  symbol: string;
  price: number;
  variation: number;
}

export type CryptoSectorEnum =
  | "Store of Value / Payment"
  | "Smart Contract"
  | "Stablecoins"
  | "DeFi"
  | "Infrastructure / L2"
  | "Others";

export interface SectorVolume {
  [key: string]: number;
}

export interface ChartData {
  name: CryptoSectorEnum | string;
  volume: number;
}
