import praw
import pandas as pd

reddit = praw.Reddit(client_id='Et0k78CT2N_TOTIn45YEog',
                     client_secret='jXrrw6fFL-0jkfuDP1oTYCD2fZvVCQ',
                     user_agent='mental_health_analysis')
                    

subreddit = reddit.subreddit('mentalhealth')
posts = subreddit.new(limit=100)

data = []
for post in posts:
    data.append({
        'title': post.title,
        'text': post.selftext,
        'score': post.score,
        'comments': post.num_comments,
        'date': post.created_utc
    })

df = pd.DataFrame(data)
df.to_csv('reddit_mental_health.csv', index=False)
print("Data saved to reddit_mental_health.csv")
