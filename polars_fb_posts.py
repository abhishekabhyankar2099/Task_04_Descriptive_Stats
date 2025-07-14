import polars as pl

FILE_PATH = 'C:/Users/Hp/Documents/OPT Research/period_03/2024_fb_posts_president_scored_anon.csv'  
def clean_numeric(df: pl.DataFrame, numeric_cols: list[str]) -> pl.DataFrame:
    for col in numeric_cols:
        df = df.with_columns(
            pl.col(col)
            .cast(pl.Utf8)
            .str.replace_all(",", "")
            .str.replace_all("-", "0")
            .cast(pl.Float64)
            .alias(col)
        )
    return df

def main():
    # Define column lists inside the main function
    numeric_cols = [
        'Total Interactions', 'Likes', 'Comments', 'Shares',
        'Love', 'Wow', 'Haha', 'Sad', 'Angry', 'Care',
        'Post Views', 'Total Views', 'Total Views For All Crossposts',
        'Overperforming Score'
    ]

    categorical_cols = ['Page Category', 'Type', 'Is Video Owner?']

    # Load the CSV
    df = pl.read_csv(FILE_PATH, infer_schema_length=1000)

    # Clean numeric columns
    df = clean_numeric(df, numeric_cols)

    # === Descriptive Stats ===
    print("\n=== Descriptive Stats (Numeric Columns) ===")
    print(df.select([pl.col(col).mean().alias(f"{col}_mean") for col in numeric_cols]))
    print(df.select([pl.col(col).min().alias(f"{col}_min") for col in numeric_cols]))
    print(df.select([pl.col(col).max().alias(f"{col}_max") for col in numeric_cols]))

    # === Value Counts (Categorical Columns) ===
    for col in categorical_cols:
        print(f"\n=== Value Counts for {col} ===")
        print(df.group_by(col).agg(pl.count()).sort("count", descending=True))

    # === Grouped by Page Category ===
    print("\n=== Grouped by Page Category (Means) ===")
    grouped = df.group_by("Page Category").agg(
        [pl.col(col).mean().round(2).alias(f"{col}_mean") for col in numeric_cols]
    )
    print(grouped)

    # === Group by Post Month if possible ===
    if 'Post Created' in df.columns:
        df = df.with_columns(
            pl.col('Post Created')
            .str.slice(0, 10)
            .str.strptime(pl.Date, "%Y-%m-%d", strict=False)
            .dt.strftime("%Y-%m")
            .alias("Post Month")
        )
        print("\n=== Grouped by Post Month ===")
        print(
            df.group_by("Post Month").agg(
                [pl.col(col).mean().round(2).alias(f"{col}_mean") for col in numeric_cols]
            )
        )

if __name__ == "__main__":
    main()
