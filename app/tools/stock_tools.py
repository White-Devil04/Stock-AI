# app/tools/stock_tools.py
from langchain.tools import BaseTool
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
import datetime
from typing import Any, Dict, Optional, Type, Union, ClassVar

class StockPriceCheckTool(BaseTool):
    name: str = "stock_price_check"
    description: str = "Useful for getting the current stock price for a given ticker symbol"
    
    _search: ClassVar[Any] = None
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        object.__setattr__(self, "_search", DuckDuckGoSearchAPIWrapper())
    
    def _run(self, ticker: str) -> str:
        """Execute the stock price check."""
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        query = f"{ticker} stock price today {current_date} market data"
        search_results = self._search.run(query)
        return search_results

    def _arun(self, ticker: str):
        """Execute the stock price check asynchronously."""
        raise NotImplementedError("This tool does not support async")