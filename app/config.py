import os
from dotenv import load_dotenv

load_dotenv()

API_TITLE = "Stock Market Agent API"
API_DESCRIPTION = "API for fetching stock information and recommendations"
API_VERSION = "1.0.0"


GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY environment variable not set")

