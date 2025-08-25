import axios from "axios";

export async function getApiMarketCap() {
    try {
        const response = await axios.get("http://127.0.0.1:8000/api/coingecko/market-cap")

        return response.data
    } catch(error: unknown) {
        if (axios.isAxiosError(error)) {
            console.error("API Error:", error.response?.data || error.message);
        }

        return [];
    }
}
