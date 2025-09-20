from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyzes the sentiment of a given text.
    Returns:
        'positive', 'negative', or 'neutral'
    """
    try:
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity  # range [-1, 1]
        
        if polarity > 0.1:
            return "positive"
        elif polarity < -0.1:
            return "negative"
        else:
            return "neutral"
    except Exception as e:
        print(f"Error analyzing sentiment: {e}")
        return "neutral"
