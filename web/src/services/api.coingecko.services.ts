import axios from "axios";
import { endpoint } from "@/models/api.coingecko.models";

export async function getApiCoinGeckoOverview() {
    try {
        const response = await axios.get(`${endpoint}/coingecko/api/overview`)
        return response.data

    } catch(error: unknown) {
        if (axios.isAxiosError(error)) {
            console.error("API Error:", error.response?.data || error.message);
        }

        return []; // spinner
    }
}

export async function getApiCoinGeckoTopCoins() {
    try {
        const response = await axios.get(`${endpoint}/coingecko/api/topcoins?limit=10&currency=usd`)
        return response.data

    } catch (error: unknown) {
        if (axios.isAxiosError(error)) {
            console.error("API Error:", error.response?.data || error.message);
        }

        return []; // spinner
    }
}
