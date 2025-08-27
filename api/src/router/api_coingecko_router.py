from typing import List
from fastapi import APIRouter, HTTPException, Query
from src.docs.response import ERROR_RESPONSES

from src.services.coingecko.coingecko_api_services import (
    get_api_overview,
    get_api_topcoins,
    get_api_market_chart,
)

from src.models.coingecko.docs_coingecko_models import (
    CoinGeckoOverviewModel,
    TopCoinModel,
)

router = APIRouter(prefix="/coingecko/api", tags=["Coingecko API"])


@router.get(
    "/overview",
    summary="Fetch CoinGecko API Overview",
    description=(
        "Fetches the latest global cryptocurrency market overview from CoinGecko, "
        "including total market capitalization, 24h trading volume, "
        "and BTC/ETH dominance percentages."
    ),
    response_model=CoinGeckoOverviewModel,
    responses=ERROR_RESPONSES,
)
def get_api_coingecko_overview(
    retries: int = Query(
        3, ge=1, description="Number of retry attempts if request fails"
    ),
    delay: float = Query(
        2.0, ge=0.0, description="Seconds to wait between retry attempts"
    ),
):
    """Endpoint to retrieve global cryptocurrency overview."""
    data = get_api_overview(retries=retries, delay=delay)

    if not data:
        raise HTTPException(
            status_code=500, detail="Unable to fetch data from CoinGecko API"
        )
    return data


@router.get(
    "/topcoins",
    summary="Fetch CoinGecko API Top Coins",
    description=(
        "Retrieves the top cryptocurrencies from CoinGecko, "
        "including name, symbol, current price, trading volume, "
        "market cap, dominance, and 24h price changes."
    ),
    response_model=List[TopCoinModel],
    responses=ERROR_RESPONSES,
)
def get_api_coingecko_topcoins(
    limit: int = Query(10, ge=1, description="Number of top coins to fetch"),
    currency: str = Query("usd", description="Currency to display prices in"),
    retries: int = Query(
        3, ge=1, description="Number of retry attempts if request fails"
    ),
    delay: float = Query(
        2.0, ge=0.0, description="Seconds to wait between retry attempts"
    ),
):
    """Endpoint to retrieve top cryptocurrencies by market capitalization."""
    data = get_api_topcoins(
        limit=limit, currency=currency, retries=retries, delay=delay
    )

    if not data:
        raise HTTPException(
            status_code=500, detail="Unable to fetch data from CoinGecko API"
        )
    return data


@router.get(
    "/marketchart",
    summary="Fetch CoinGecko Market Chart Data",
    description=(
        "Retrieves historical market data for a specific cryptocurrency from CoinGecko, "
        "including price, market capitalization, and trading volume over a specified number of days."
    ),
    responses=ERROR_RESPONSES,
)
def get_api_coingecko_market_chart(
    coin_id: str = Query(..., description="The CoinGecko ID of the cryptocurrency"),
    days: int = Query(30, description="Number of past days to retrieve data for"),
    currency: str = Query("usd", description="Currency to display prices in"),
):
    data = get_api_market_chart(coin_id=coin_id, days=days, currency=currency)
    if not data:
        raise HTTPException(status_code=500, detail="Unable to fetch market chart data")
    return data
