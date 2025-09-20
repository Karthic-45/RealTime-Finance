import yfinance as yf

def fetch_stock_price(symbol):
    try:
        stock = yf.Ticker(symbol)
        data = stock.history(period="1d")

        if data.empty:
            return {"symbol": symbol, "price": 0.0, "change": 0.0}

        # Latest close price
        price = float(data["Close"].iloc[-1])

        # Previous close for % change
        if len(data) > 1:
            prev_close = float(data["Close"].iloc[-2])
        else:
            prev_close = price

        change = ((price - prev_close) / prev_close) * 100 if prev_close > 0 else 0.0

        return {"symbol": symbol, "price": price, "change": change}

    except Exception as e:
        print(f"⚠️ Error fetching stock {symbol}: {e}")
        return {"symbol": symbol, "price": 0.0, "change": 0.0}
