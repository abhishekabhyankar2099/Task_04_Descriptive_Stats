import polars as pl

FILE_PATH = 'C:/Users/Hp/Documents/OPT Research/period_03/2024_fb_ads_president_scored_anon.csv'  

def clean_numeric(df: pl.DataFrame, cols: list[str]) -> pl.DataFrame:
    for col in cols:
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
    # Define columns
    numeric_cols = [
        'estimated_audience_size',
        'estimated_impressions',
        'estimated_spend'
    ]
    categorical_cols = ['currency', 'publisher_platforms']

    # Load data
    df = pl.read_csv(FILE_PATH, infer_schema_length=1000)

    # Clean numeric columns
    df = clean_numeric(df, numeric_cols)

    # === Descriptive Stats ===
    print("\n=== Descriptive Stats (Numeric Columns) ===")
    for stat in ["mean", "min", "max"]:
        print(f"\n{stat.upper()}s:")
        print(df.select([getattr(pl.col(c), stat)().alias(f"{c}_{stat}") for c in numeric_cols]))

    # === Categorical Stats ===
    for col in categorical_cols:
        print(f"\n=== Value Counts for {col} ===")
        print(df.group_by(col).agg(pl.count()).sort("count", descending=True))

    # === Grouped by page_id ===
    print("\n=== Grouped by page_id ===")
    grouped = df.group_by("page_id").agg(
        [pl.col(c).mean().round(2).alias(f"{c}_mean") for c in numeric_cols]
    )
    print(grouped)

    # === Optional: Grouped by (page_id, ad_id) ===
    print("\n=== Grouped by (page_id, ad_id) ===")
    grouped_nested = df.group_by(["page_id", "ad_id"]).agg(
        [pl.col(c).mean().round(2).alias(f"{c}_mean") for c in numeric_cols]
    )
    print(grouped_nested)

if __name__ == "__main__":
    main()
