from flask import Flask, jsonify, render_template
from flask_cors import CORS
import threading
import os
import pathway as pw

# Import Pathway tables and writers
from pathways_pipeline import stocks, news, insights, stock_writer, news_writer

app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), "../frontend/templates")
)

CORS(app, resources={r"/api/*": {"origins": "*"}})

# --- Start writers ---
threading.Thread(target=stock_writer, daemon=True).start()
threading.Thread(target=news_writer, daemon=True).start()

# --- Start the Pathway engine in a background thread ---
def run_pathway():
    pw.run()

threading.Thread(target=run_pathway, daemon=True).start()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/stocks")
def get_stocks():
    return jsonify(stocks.collect())       # take a snapshot

@app.route("/api/news")
def get_news():
    return jsonify(news.collect())

@app.route("/api/insights")
def get_insights():
    return jsonify(insights.collect())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
