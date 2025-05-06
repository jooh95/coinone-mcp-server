import requests

async def get_orderbook(quote_currency: str = "KRW", target_currency: str = "BTC") -> dict:
    """Get the current orderbook for a specific market.
    Args:
        quote_currency (str, optional): Market base currency. Default is 'KRW'.
        target_currency (str, optional): Symbol of the asset to query. Default is 'BTC'.
    Returns:
        dict: API response
    """
    url = f"https://api.coinone.co.kr/orderbook?quote_currency={quote_currency}&target_currency={target_currency}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}
