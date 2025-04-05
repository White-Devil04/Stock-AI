# app/main.py
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import os
import uvicorn


from app.agent.stock_agent import StockMarketAgent
from app.config import API_TITLE, API_DESCRIPTION, API_VERSION, GROQ_API_KEY


app = FastAPI(
    title=API_TITLE,
    description=API_DESCRIPTION,
    version=API_VERSION,
)

class StockRequest(BaseModel):
    ticker: str

class StockResponse(BaseModel):
    ticker: str
    price: str
    analysis: str

def get_agent():
    return StockMarketAgent(api_key=GROQ_API_KEY)

@app.post("/stock", response_model=StockResponse)
async def get_stock_info(request: StockRequest, agent: StockMarketAgent = Depends(get_agent)):
    """
    Get stock information and recommendation for a given ticker.
    
    Parameters:
    - ticker: The stock ticker symbol (e.g., AAPL, MSFT, GOOGL)
    
    Returns:
    - ticker: The requested stock ticker
    - price: The current stock price
    - analysis: Analysis including current price, trends, and buy/sell/hold recommendation
    """
    try:
        result = agent.get_stock_info(request.ticker)
        return {
            "ticker": result["ticker"],
            "price": result["price"],
            "analysis": result["analysis"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)