import pandas as pd

FILE_PATH = 'C:/Users/Hp/Documents/OPT Research/period_03/2024_tw_posts_president_scored_anon.csv'

def main():
    df = pd.read_csv(FILE_PATH)

    # Convert timestamp
    df['createdAt'] = pd.to_datetime(df['createdAt'], errors='coerce')

    # Descriptive stats
    print("\n=== Descriptive Stats (Numerical) ===")
    print(df[['retweetCount', 'replyCount', 'likeCount', 'quoteCount', 'viewCount', 'bookmarkCount']].describe())

    print("\n=== Categorical Value Counts ===")
    for col in ['source', 'lang', 'isReply', 'isRetweet', 'isQuote']:
        print(f"\n{col}:\n", df[col].value_counts())

    print("\n=== Grouped by month_year (mean engagement) ===")
    print(df.groupby("month_year")[['retweetCount', 'replyCount', 'likeCount', 'quoteCount']].mean().round(2))

if __name__ == "__main__":
    main()
