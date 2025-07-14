import pandas as pd

FILE_PATH = 'C:/Users/Hp/Documents/OPT Research/period_03/2024_fb_ads_president_scored_anon.csv'  

def clean_numeric(df, cols):
    for col in cols:
        df[col] = df[col].astype(str).str.replace(",", "").replace("-", "0")
        df[col] = pd.to_numeric(df[col], errors="coerce")
    return df

def main():
    # Load the CSV
    df = pd.read_csv(FILE_PATH)

    # Define columns
    numeric_cols = [
        'estimated_audience_size',
        'estimated_impressions',
        'estimated_spend'
    ]
    categorical_cols = ['currency', 'publisher_platforms']

    # Clean and convert numeric columns
    df = clean_numeric(df, numeric_cols)

    # === Descriptive Stats ===
    print("\n=== Descriptive Stats (Numeric) ===")
    print(df[numeric_cols].describe().round(2))

    # === Categorical Stats ===
    print("\n=== Categorical Value Counts ===")
    for col in categorical_cols:
        print(f"\n{col}:\n", df[col].value_counts())

    # === Group by page_id ===
    print("\n=== Grouped by page_id (mean values) ===")
    print(df.groupby("page_id")[numeric_cols].mean().round(2))

    # === Optional: Group by (page_id, ad_id) ===
    print("\n=== Grouped by (page_id, ad_id) ===")
    print(df.groupby(["page_id", "ad_id"])[numeric_cols].mean().round(2))

if __name__ == "__main__":
    main()
