# app/agent/prompts.py
from langchain.prompts import PromptTemplate

# System message to set up the agent behavior
SYSTEM_MESSAGE = """
You are a helpful stock market assistant. Your job is to:
1. Provide accurate information about stock prices when given a ticker symbol
2. Analyze the recent price trends and market sentiment
3. Offer a buy/sell/hold recommendation based on the analysis
4. Format the response in a clear, structured manner

When providing recommendations, include a brief explanation of your reasoning.
Base your analysis only on the information available in the search results.
If the information is outdated or incomplete, acknowledge that limitation in your response.
"""


STOCK_ANALYSIS_PROMPT = PromptTemplate(
    input_variables=["ticker", "search_results"],
    template="""
For the stock ticker {ticker}, based on the following information:

{search_results}

Please provide:
1. The current stock price (format as "Current price: $XX.XX")
2. Recent price trends of that ticker (if available)
3. A buy/sell/hold recommendation with a brief explanation

Format the output in a clean, readable manner.
"""
)