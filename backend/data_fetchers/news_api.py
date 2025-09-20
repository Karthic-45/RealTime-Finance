import requests
from config import NEWS_API_KEY, NEWS_QUERY

BASE_URL = "https://newsapi.org/v2/everything"

def fetch_latest_news():
    try:
        params = {
            "q": NEWS_QUERY,
            "sortBy": "publishedAt",
            "apiKey": NEWS_API_KEY,
            "pageSize": 5
        }
        res = requests.get(BASE_URL, params=params)
        articles = res.json().get("articles", [])
        return [
            {
                "title": a["title"],
                "description": a["description"],
                "source": a["source"]["name"],
                "publishedAt": a["publishedAt"]
            } for a in articles
        ]
    except Exception as e:
        print(f"Error fetching news: {e}")
        return []
