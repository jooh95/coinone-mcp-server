import httplib2
from typing import Optional
from config import COINONE_ACCESS_TOKEN, COINONE_SECRET_KEY, get_encoded_payload, get_signature

async def cancel_order(
    quote_currency: str,
    target_currency: str,
    order_id: str = None,
    user_order_id: str = None
) -> dict:
    """Cancel a Coinone order.
    Args:
        quote_currency (str): Market base currency. e.g., 'KRW'.
        target_currency (str): Symbol of the asset to order. e.g., 'BTC'.
        order_id (str, optional): Order ID (UUID format)
        user_order_id (str, optional): User-defined order ID. Either order_id or user_order_id is required. Up to 150 characters, supports lowercase letters/numbers/special characters (_ .)
    Returns:
        dict: API response. On success, returns canceled order info.
    """
    if not order_id and not user_order_id:
        return {"error": "Either order_id or user_order_id must be provided"}
    
    url = "https://api.coinone.co.kr/v2.1/order/cancel"
    access_token = COINONE_ACCESS_TOKEN
    secret_key = COINONE_SECRET_KEY
    if not access_token or not secret_key:
        return {"error": "API key and secret must be provided either as arguments or in config.py/.env"}
    
    body = {
        "access_token": access_token,
        "quote_currency": quote_currency,
        "target_currency": target_currency
    }
    
    if order_id:
        body["order_id"] = order_id
    if user_order_id:
        body["user_order_id"] = user_order_id
        
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
