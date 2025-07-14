
import polars as pl

FILE_PATH = 'C:/Users/Hp/Documents/OPT Research/period_03/2024_tw_posts_president_scored_anon.csv'

def main():
    df = pl.read_csv(FILE_PATH)

    numeric_cols = ['retweetCount', 'replyCount', 'likeCount', 'quoteCount', 'viewCount', 'bookmarkCount']

    print("\n=== Descriptive Stats (Numeric) ===")
    print(df.select([pl.col(c).mean().alias(f"{c}_mean") for c in numeric_cols]))
    print(df.select([pl.col(c).min().alias(f"{c}_min") for c in numeric_cols]))
    print(df.select([pl.col(c).max().alias(f"{c}_max") for c in numeric_cols]))

    print("\n=== Value Counts (Categorical) ===")
    for col in ['source', 'lang', 'isReply', 'isRetweet']:
        print(f"\n{col}:\n", df.group_by(col).count())

    print("\n=== Grouped by month_year ===")
    grouped = df.group_by("month_year").agg([pl.col(c).mean().round(2) for c in numeric_cols])
    print(grouped)

if __name__ == "__main__":
    main()
