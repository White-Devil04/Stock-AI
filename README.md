# Stock-AI API Platform

Stock-AI is an advanced API platform designed for stock market analysis and predictions using artificial intelligence algorithms.

## Features

- Real-time stock data analysis
- Historical price trend visualization
- Predictive analytics for stock movements
- Portfolio optimization recommendations
- Market sentiment analysis

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Setup

1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/Stock-AI.git
   cd Stock-AI
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On Unix or MacOS
   source venv/bin/activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

## Running Locally

1. Start the server
   ```bash
   uvicorn main:app --reload
   ```

2. Access the API at `http://127.0.0.1:8000`

3. View API documentation at `http://127.0.0.1:8000/docs`

## Deployed API

The API is deployed and available at:
[https://stock-ai-y76m.onrender.com](https://stock-ai-y76m.onrender.com)

You can access the API documentation at:
[https://stock-ai-y76m.onrender.com/docs](https://stock-ai-y76m.onrender.com/docs)



## Testing with Unicorn

The Stock-AI API is built using FastAPI and can be tested with Unicorn for HTTP request handling.

### Running Tests

1. Run the test suite
   ```bash
   python -m pytest tests/
   ```

2. For specific test cases
   ```bash
   python -m pytest tests/test_stock_api.py
   ```

### Manual Testing

You can test the API endpoints directly using curl or any API testing tool:

```bash
curl -X GET "https://stock-ai-y76m.onrender.com/api/stock/AAPL" -H "accept: application/json"
```

## Example Usage

### Fetching Apple Stock Data

```python
import requests

# Local development
url = "http://127.0.0.1:8000/api/stock/AAPL"

# Production
# url = "https://stock-ai-y76m.onrender.com/api/stock/AAPL"

response = requests.get(url)
data = response.json()

print(f"Current Price: ${data['price']}")
print(f"Change: {data['change']}%")
print(f"Market Cap: ${data['market_cap']}")
```

### Sample Response

```json
{
  "ticker": "AAPL",
  "price": "217.90",
  "analysis": "Here is the information you requested:\n\n**Current Stock Price:**\nCurrent price: $217.90\n\n**Recent Price Trends:**\nThe stock has been trending upwards in the short term, with a 2.10% increase on Feb 04, 2025, and a slight decrease of 0.14% on Feb 05, 2025. However, the stock is still down 12.4% for the year.\n\n**Buy/Sell/Hold Recommendation:**\nHold\n\nThe recent price trends suggest that the stock is experiencing some volatility, but the overall trend is still downwards. With a 12.4% decline for the year, it may be wise to hold off on buying until the stock shows more consistent signs of recovery. However, if you already hold AAPL stock, it may be worth holding onto it for now, as the company's fundamentals are still strong."
}
```

## Error Handling

The API returns standard HTTP status codes:

- 200: Success
- 400: Bad request
- 404: Stock symbol not found
- 500: Server error

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
