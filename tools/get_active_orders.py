import httplib2
from typing import Optional, List
from config import COINONE_ACCESS_TOKEN, COINONE_SECRET_KEY, get_encoded_payload, get_signature

async def get_active_orders(
    quote_currency: str = None,
    target_currency: str = None,
    order_type: List[str] = None
) -> dict:
    """Get the list of open (active) orders on Coinone.
    Args:
        quote_currency (str, optional): Market base currency. e.g., 'KRW'.
        target_currency (str, optional): Symbol of the asset to order. e.g., 'BTC'.
        order_type (List[str], optional): Order types to query. ['LIMIT'], ['STOP_LIMIT'], ['LIMIT', 'STOP_LIMIT'], etc.
    Returns:
        dict: List of open orders or error message
    """
    url = "https://api.coinone.co.kr/v2.1/order/active_orders"
    access_token = COINONE_ACCESS_TOKEN
    secret_key = COINONE_SECRET_KEY
    if not access_token or not secret_key:
        return {"error": "API key and secret must be provided either as arguments or in config.py/.env"}
    body = {
        "access_token": access_token
    }
    if quote_currency is not None:
        body["quote_currency"] = quote_currency
    if target_currency is not None:
        body["target_currency"] = target_currency
    if order_type is not None:
        body["order_type"] = order_type
    encoded_payload = get_encoded_payload(body)
    headers = {
        'Content-type': 'application/json',
        'X-COINONE-PAYLOAD': encoded_payload,
        'X-COINONE-SIGNATURE': get_signature(encoded_payload),
    }
    http = httplib2.Http()
    response, content = http.request(url, 'POST', headers=headers)
    try:
        return content
    except Exception as e:
        return {"error": str(e)}
