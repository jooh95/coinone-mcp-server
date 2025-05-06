import os
import uuid
import base64
import hmac
import hashlib
import json
from dotenv import load_dotenv

load_dotenv()

COINONE_ACCESS_TOKEN = os.getenv("COINONE_ACCESS_TOKEN")
COINONE_SECRET_KEY = bytes(os.getenv("COINONE_SECRET_KEY"), 'utf-8')

def get_encoded_payload(payload):
    payload['nonce'] = str(uuid.uuid4())
    dumped_json = json.dumps(payload)
    print(dumped_json)
    encoded_json = base64.b64encode(bytes(dumped_json, 'utf-8'))
    return encoded_json


def get_signature(encoded_payload):
    signature = hmac.new(COINONE_SECRET_KEY, encoded_payload, hashlib.sha512)
    return signature.hexdigest()
