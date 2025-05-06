from typing import Optional
from config import COINONE_ACCESS_TOKEN, COINONE_SECRET_KEY, get_encoded_payload, get_signature
import httplib2

async def place_order(
    side: str = None,
    quote_currency: str = None,
    target_currency: str = None,
    type: str = None,
    price: str = None,
    qty: str = None,
    amount: str = None,
    post_only: bool = None,
    limit_price: str = None,
    trigger_price: str = None,
    user_order_id: str = None
) -> dict:
    """Place an order on Coinone using the v2.1 order API.
    Args:
        side (str, required): Order direction. 'BUY' (buy) or 'SELL' (sell). Required for all order types.
        quote_currency (str, required): Market base currency. e.g., 'KRW'. Required for all order types.
        target_currency (str, required): Symbol of the asset to order. e.g., 'BTC'. Required for all order types.
        type (str, required): Order type. 'LIMIT', 'MARKET', 'STOP_LIMIT'. Required for all order types.
        price (str, optional): Order price. Required for limit and stop-limit orders.
        qty (str, optional): Order quantity. Required for limit, stop-limit, and market sell orders. Truncated if below minimum unit.
        amount (float): Total order amount. Required for market buy orders. Truncated if below minimum unit (0.0001 KRW). e.g., 5000, 10000.50. Required for market buy.
        post_only (bool, optional): Post Only order. Required for limit orders.
        limit_price (str, optional): Maximum/minimum execution price (ceiling/floor). Used for market orders.
        trigger_price (str, optional): Trigger price for stop-limit orders. Required for stop-limit.
        user_order_id (str, optional): User-defined order ID. Up to 150 characters, supports lowercase letters/numbers/special characters (_ .). Must be unique across all pairs.
    Returns:
        dict: API response. 'success' on success, 'error' and error code on failure.
    """
    url = "https://api.coinone.co.kr/v2.1/order"
    access_token = COINONE_ACCESS_TOKEN
    secret_key = COINONE_SECRET_KEY
    if not access_token or not secret_key:
        return {"error": "API key and secret must be provided either as arguments or in config.py/.env"}
    body = {
        "access_token": access_token,
        "side": side,
        "quote_currency": quote_currency,
        "target_currency": target_currency,
        "type": type
    }
    if price is not None:
        body["price"] = price
    if qty is not None:
        body["qty"] = qty
    if amount is not None:
        body["amount"] = amount
    if post_only is not None:
        body["post_only"] = post_only
    if limit_price is not None:
        body["limit_price"] = limit_price
    if trigger_price is not None:
        body["trigger_price"] = trigger_price
    if user_order_id is not None:
        body["user_order_id"] = user_order_id

    encoded_payload = get_encoded_payload(body)

    headers = {
        'Content-type': 'application/json',
        'X-COINONE-PAYLOAD': encoded_payload,
        'X-COINONE-SIGNATURE': get_signature(encoded_payload),
    }

    http = httplib2.Http()
    response, content = http.request(url, 'POST', headers=headers)

    return content

