import pandas as pd
from textblob import TextBlob

# Load cleaned data
df = pd.read_csv('cleaned_reddit_mental_health.csv')

# Define function to get sentiment polarity
def analyze_sentiment(text):
    return TextBlob(str(text)).sentiment.polarity  # returns value between -1.0 (neg) to +1.0 (pos)

# Apply sentiment analysis on the 'text' column
df['sentiment_score'] = df['text'].apply(analyze_sentiment)

# Categorize based on polarity
def sentiment_category(score):
    if score > 0.1:
        return 'Positive'
    elif score < -0.1:
        return 'Negative'
    else:
        return 'Neutral'

df['sentiment'] = df['sentiment_score'].apply(sentiment_category)

# Save results
df.to_csv('reddit_sentiment_analysis.csv', index=False)
print("Sentiment analysis complete and saved to reddit_sentiment_analysis.csv")
