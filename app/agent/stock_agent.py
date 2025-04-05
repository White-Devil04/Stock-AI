# app/agent/stock_agent.py
from langchain.agents import initialize_agent, AgentType
from langchain_groq import ChatGroq
from langchain.schema import SystemMessage
from langchain.memory import ConversationBufferMemory
import re

from app.tools.stock_tools import StockPriceCheckTool
from app.agent.prompts import SYSTEM_MESSAGE, STOCK_ANALYSIS_PROMPT

class StockMarketAgent:
    def __init__(self, api_key):
        self.llm = ChatGroq(
            api_key=api_key,
            model_name="llama3-70b-8192", 
            temperature=0.2  
        )
        
        self.tools = [StockPriceCheckTool()]
        
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        
        self.agent = initialize_agent(
            tools=self.tools,
            llm=self.llm,
            agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
            verbose=True,
            memory=self.memory,
            system_message=SYSTEM_MESSAGE,
        )
    
    def get_stock_info(self, ticker):
        search_tool = self.tools[0]
        search_results = search_tool._run(ticker)
        
        prompt = STOCK_ANALYSIS_PROMPT.format(
            ticker=ticker,
            search_results=search_results
        )
        
        # Generate response using the LLM
        response = self.llm.invoke(prompt)

        content = response.content
        price = "N/A"

        price_match = re.search(r"Current price:?\s*\$?([0-9]+\.[0-9]+)", content)
        if price_match:
            price = price_match.group(1)
        
        return {
            "ticker": ticker,
            "price": price,
            "analysis": content
        }