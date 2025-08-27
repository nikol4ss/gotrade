import axios, { AxiosError } from "axios";
import type { CoinGeckoOverview, CoinGeckoCoin  } from "@/models/api.coingecko.models";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000/coingecko/api",
});


/**
 * Fetches a global overview of the cryptocurrency market from CoinGecko with retry logic.
 *
 * @param retries - Number of retry attempts (default: 3)
 * @param delay - Delay between retries in seconds (default: 2)
 * @returns {Promise<CoinGeckoOverview>} Overview data
 * @throws {Error} Failed to fetch CoinGecko overview after retries
 */
export async function getApiCoinGeckoOverview(
  retries: number = 3,
  delay: number = 2
): Promise<CoinGeckoOverview> {
  for (let attempt = 0; attempt < retries; attempt++) {
    try {
      const response = await api.get<CoinGeckoOverview>("/overview");
      return response.data;
    } catch (error: unknown) {
      if (axios.isAxiosError(error)) {
        console.error(
          `API Error (attempt ${attempt + 1}):`,
          error.response?.data || error.message
        );
      }
      if (attempt < retries - 1) {
        await new Promise(res => setTimeout(res, delay * 1000));
      } else {
        throw new Error("Failed to fetch CoinGecko overview after retries");
      }
    }
  }
  throw new Error("Unexpected error in getApiCoinGeckoOverview");
}


/**
 * Fetches top cryptocurrencies by market data from CoinGecko.
 *
 * @param limit - Number of coins to fetch (default: 10)
 * @param currency - Currency for prices (default: "usd")
 * @returns {Promise<CoinGeckoCoin[]>} List of coins
 * @throws {Error} Failed to fetch CoinGecko top coins
 */
export async function getApiCoinGeckoTopCoins(
  limit: number = 10,
  currency: string = "usd"
): Promise<CoinGeckoCoin[]> {
  try {
    const response = await api.get<CoinGeckoCoin[]>(
      `/topcoins?limit=${limit}&currency=${currency}`
    );
      return response.data;

  } catch (error: unknown) {
    if (axios.isAxiosError(error)) {
      const err = error as AxiosError;
      console.error("API Error:", err.response?.data || err.message);
    }

    throw new Error("Failed to fetch CoinGecko top coins");
  }
}


// export async function getApiCoinGeckoMarkeChart(coin_id: string, days: number) {
//     // http://127.0.0.1:8000/coingecko/api/marketchart?coin_id=bitcoin&days=5&currency=usd&retries=3&delay=2

//     try
// }
