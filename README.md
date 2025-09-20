# Trading AI Backend

This project provides a **Flask-based backend** for real-time trading insights using:
- [Pathway](https://pathway.com) for streaming data pipelines
- OpenAI for AI-powered insights
- yFinance for stock data
- TextBlob for sentiment analysis
- Docker for containerized deployment

---

## 🚀 Features
- Fetches real-time stock prices
- Analyzes financial news for sentiment
- Generates trading insights using AI
- Provides REST APIs for frontend integration

---

## 🛠️ Project Structure
trading_ai/
│── backend/
│ ├── app.py # Flask entrypoint
│ ├── pathways_pipeline.py # Pathway data pipeline
│ ├── data_fetchers/ # Stock & news APIs
│ ├── config.py # Config & environment variables
│── requirements.txt # Python dependencies
│── Dockerfile # Backend image definition
│── docker-compose.yml # Multi-service orchestration
│── .env # Environment variables (not committed)
