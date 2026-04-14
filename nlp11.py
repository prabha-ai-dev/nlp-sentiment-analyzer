from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()
reviews = [
    "I love this phone, amazing battery!",
    "Worst product ever, waste of money",
    "It's okay, not bad",
    "Absolutely fantastic!",
    "Very disappointing experience",
    "Good value for money",
    "Not worth it",
    "Excellent quality",
    "Average product",
    "I hate it"
]
for review in reviews:
    score = sia.polarity_scores(review)
    if score['compound'] > 0:
        sentiment = "positive"
    elif score['compound'] < 0:
        sentiment = "negative"
    else: 
        sentiment = "neutral"
    print(review, '-', sentiment)
