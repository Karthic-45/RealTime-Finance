import os

ALPHA_VANTAGE_KEY = os.getenv("ALPHA_VANTAGE_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
STOCK_SYMBOLS = ["TSLA", "AAPL", "AMZN"]  # you can add more
NEWS_QUERY = "stock OR finance OR company"
