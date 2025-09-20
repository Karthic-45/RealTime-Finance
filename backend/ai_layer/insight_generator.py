from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_insight(stock_data):
    """
    stock_data: dict with 'symbol', 'price', 'change'
    """
    try:
        prompt = f"Explain in simple English why {stock_data['symbol']} stock is {stock_data['change']}% at ${stock_data['price']} today."
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error generating insight: {e}")
        return "No insight available"
