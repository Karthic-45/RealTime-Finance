import pathway as pw
from data_fetchers.stock_api import fetch_stock_price
from data_fetchers.news_api import fetch_latest_news
from ai_layer.insight_generator import generate_insight
from ai_layer.sentiment_analysis import analyze_sentiment
from config import STOCK_SYMBOLS
import time
import threading

# --- Step 1: Define schemas ---
class StockSchema(pw.Schema):
    symbol: str
    price: float
    timestamp: float

class NewsSchema(pw.Schema):
    title: str
    description: str
    url: str
    publishedAt: str
    sentiment: str

# --- Step 2: Create empty (streaming) tables ---
stocks = pw.io.python.read(StockSchema)
news = pw.io.python.read(NewsSchema)

# --- Step 3: Derive tables with Pathway operators ---
insights = stocks.select(
    symbol=stocks.symbol,
    insight=pw.apply(generate_insight, stocks)
)

# Example: join news + stocks if you ever need
# joined = stocks.join(news, stocks.symbol == news.symbol)

# --- Step 4: Writer threads to push rows into Pathway ---
def stock_writer():
    while True:
        for symbol in STOCK_SYMBOLS:
            s = fetch_stock_price(symbol)
            if s:
                stocks.send(
                    symbol=s["symbol"],
                    price=s["price"],
                    timestamp=time.time(),
                )
        time.sleep(30)

def news_writer():
    while True:
        for a in fetch_latest_news():
            sentiment = analyze_sentiment(
                a.get("description") or a.get("title", "")
            )
            news.send(
                title=a.get("title", ""),
                description=a.get("description", ""),
                url=a.get("url", ""),
                publishedAt=a.get("publishedAt", ""),
                sentiment=sentiment,
            )
        time.sleep(30)

# --- Step 5: Start Pathway and the writers ---
if __name__ == "__main__":
    t1 = threading.Thread(target=stock_writer, daemon=True)
    t2 = threading.Thread(target=news_writer, daemon=True)
    t1.start()
    t2.start()

    # Run Pathway's engine (blocking)
    pw.run()
