import axios from "axios";
import type { Coin } from "@/models/api.binance.models";

export async function getApiCoin(): Promise<Coin[]> {
  try {
    const response = await axios.get<Coin[]>("http://127.0.0.1:8000/api/binance/top-coins");
    return response.data;

  } catch (error: unknown) {
    if (axios.isAxiosError(error)) {
        console.error("API Error:", error.response?.data || error.message);
      }

    return [];
  }
}
