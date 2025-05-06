import httplib2
from config import COINONE_ACCESS_TOKEN, COINONE_SECRET_KEY, get_encoded_payload, get_signature

async def get_balance() -> dict:
    """Get all Coinone balances.
    Returns:
        dict: All balance information or error message
    """
    url = "https://api.coinone.co.kr/v2.1/account/balance/all"
    access_token = COINONE_ACCESS_TOKEN
    secret_key = COINONE_SECRET_KEY
    if not access_token or not secret_key:
        return {"error": "API key and secret must be provided either as arguments or in config.py/.env"}
    body = {
        "access_token": access_token
    }
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
