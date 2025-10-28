import pandas as pd
import re

# Load your CSV file
df = pd.read_csv('reddit_mental_health.csv')

# 1. Remove any rows with empty or very short text (less than 10 chars)
df = df[df['text'].str.strip().astype(bool)]
df = df[df['text'].str.len() > 10]

# 2. Remove duplicates based on title and text
df = df.drop_duplicates(subset=['title', 'text'])

# 3. Remove special characters, links, and keep only normal text
def clean_text(text):
    text = str(text)
    text = re.sub(r'http\S+', '', text)               # Remove URLs
    text = re.sub(r'[^A-Za-z0-9\s.,!?\'\"]', '', text) # Keep letters, numbers, some punctuation
    text = text.strip()
    return text

df['text'] = df['text'].apply(clean_text)
df['title'] = df['title'].apply(clean_text)

# 4. Convert all text to lowercase
df['text'] = df['text'].str.lower()
df['title'] = df['title'].str.lower()

# 5. Save cleaned data
df.to_csv('cleaned_reddit_mental_health.csv', index=False)
print("Cleaned data saved to cleaned_reddit_mental_health.csv")
