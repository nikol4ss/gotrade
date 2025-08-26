from fastapi import APIRouter, HTTPException, Query

from src.docs.response import ERROR_RESPONSES

from src.services.coingecko.coingecko_api_services import get_api_overview, get_api_topcoins
from src.models.coingecko.docs_coingecko_models import (
    CoinGeckoOverviewModel,
    TopCoinModel,
)

router = APIRouter(prefix="/coingecko/api", tags=["Coingecko API"])


@router.get(
    "/overview",
    summary="Fetch CoinGecko API Overview",
    description=(
        "Retrieves the latest overview data from the CoinGecko API, "
        "including market dominance, total market capitalization, "
        "and trading volumes for major cryptocurrencies."
    ),
    response_model=CoinGeckoOverviewModel,
    responses=ERROR_RESPONSES,
)
def get_api_coingecko_overview():
    data = get_api_overview()

    if not data:
        raise HTTPException(status_code=500, detail="Unable to fetch data")
    return data


@router.get(
    "/topcoins",
    summary="Fetch CoinGecko API Top Coins",
    description=(
        "Retrieves the top cryptocurrencies from CoinGecko, "
        "including name, symbol, current price, and trading volume."
    ),
    response_model=TopCoinModel,
    responses=ERROR_RESPONSES,
)
def get_api_coingecko_topcoins(
    limit: int = Query(10, description="Number of top coins to fetch"),
    currency: str = Query("usd", description="Currency to display prices in"),
):
    data = get_api_topcoins(limit=limit, currency=currency)
    if not data:
        raise HTTPException(status_code=500, detail="Unable to fetch data")
    return data
