import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load sentiment-analyzed data
df = pd.read_csv('reddit_sentiment_analysis.csv')

# Plot sentiment category counts
plt.figure(figsize=(8,5))
sns.countplot(x='sentiment', data=df, order=['Positive', 'Neutral', 'Negative'])
plt.title('Sentiment Distribution of Reddit Posts on Mental Health')
plt.xlabel('Sentiment')
plt.ylabel('Number of Posts')
plt.tight_layout()
plt.savefig('sentiment_distribution.png')
plt.show()

# Plot sentiment score histogram
plt.figure(figsize=(8,5))
sns.histplot(df['sentiment_score'], bins=30, kde=True, color='purple')
plt.title('Sentiment Score Distribution')
plt.xlabel('Sentiment Score')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('sentiment_score_histogram.png')
plt.show()
