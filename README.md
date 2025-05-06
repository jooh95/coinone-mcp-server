# coinone-mcp-server

This project provides a server-side implementation of the [Coinone](https://coinone.co.kr/) Cryptocurrency Exchange OpenAPI using the Model Context Protocol (MCP). It offers comprehensive tools including the retrieval of market data, access to account balance information, order creation and cancellation.

## Setup

1. Create a virtual environment using uv:
```bash
uv venv
```

2. Activate the virtual environment:
```bash
# On Unix/MacOS:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate
```

3. Install the package in development mode:
```bash
uv pip install -e .
```

## Environment Variables

To use the Coinone API, set the following environment variables in a `.env` file:

```
COINONE_ACCESS_TOKEN=your_access_token
COINONE_SECRET_KEY=your_secret_key
```

## Config the MCP Server

To config the MCP server, you can use:

```json
{
  "mcpServers": {
    "coinone-mcp-server": {
      "command": "/full/path/to/coinone-mcp-server/.venv/bin/python",
      "args": [
        "/full/path/to/coinone-mcp-server/main.py"
      ]
    }
  }
}
```

## Available Tools

| Tool                       | Description                                    |
| -------------------------- | ----------------------------------------------- |
| `place_order`                | Place an order on Coinone.  |
| `get_orderbook`           | Get the current orderbook (market prices) for a specific market.                            |
| `get_balance`        | Retrieve all Coinone balances.                      |
| `get_active_orders`    | Get a list of open (active) orders.                      |
| `cancel_order`     | Cancel an order.                   |
---

## Caution
- This server is capable of executing live trades; therefore, exercise caution when using it.
- Ensure that your API keys are stored securely and never expose them in public repositories.

## License

[Apache 2.0](LICENSE) 
