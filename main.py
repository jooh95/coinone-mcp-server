from mcp.server.fastmcp import FastMCP
import requests
import uuid
import base64
import hmac
import hashlib
import json
from typing import Optional
from typing import List
import os
from dotenv import load_dotenv
import httplib2
from config import COINONE_ACCESS_TOKEN, COINONE_SECRET_KEY
from tools.place_order import place_order
from tools.get_orderbook import get_orderbook
from tools.get_balance import get_balance
from tools.get_active_orders import get_active_orders
from tools.cancel_order import cancel_order

mcp = FastMCP("Coinone MCP Server")

mcp.tool()(place_order)
mcp.tool()(get_orderbook)
mcp.tool()(get_balance)
mcp.tool()(get_active_orders)
mcp.tool()(cancel_order)

if __name__ == "__main__":
    mcp.run()
