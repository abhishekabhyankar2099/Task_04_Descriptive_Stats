import pandas as pd

FILE_PATH = 'C:/Users/Hp/Documents/OPT Research/period_03/2024_fb_posts_president_scored_anon.csv'  # Update if needed

def clean_numeric_columns(df, columns):
    for col in columns:
        df[col] = df[col].astype(str).str.replace(",", "").replace("-", "0")
        df[col] = pd.to_numeric(df[col], errors='coerce')
    return df

def main():
    # Load the CSV
    df = pd.read_csv(FILE_PATH)

    # Define numeric and categorical columns
    numeric_cols = [
        'Total Interactions', 'Likes', 'Comments', 'Shares',
        'Love', 'Wow', 'Haha', 'Sad', 'Angry', 'Care',
        'Post Views', 'Total Views', 'Total Views For All Crossposts',
        'Overperforming Score'
    ]
    categorical_cols = ['Page Category', 'Type', 'Is Video Owner?']

    # Clean and convert numeric fields
    df = clean_numeric_columns(df, numeric_cols)

    # Basic numeric stats
    print("\n=== Descriptive Stats (Numerical) ===")
    print(df[numeric_cols].describe().round(2))

    # Categorical stats
    print("\n=== Categorical Column Frequencies ===")
    for col in categorical_cols:
        print(f"\n{col}:\n", df[col].value_counts())

    # Grouped mean stats by Page Category
    print("\n=== Grouped by Page Category (mean values) ===")
    print(df.groupby('Page Category')[numeric_cols].mean().round(2))

    # Optional: convert Post Created to datetime
    if 'Post Created' in df.columns:
        df['Post Created'] = pd.to_datetime(df['Post Created'], errors='coerce')
        df['Post Month'] = df['Post Created'].dt.to_period("M")
        print("\n=== Grouped by Post Month (mean values) ===")
        print(df.groupby('Post Month')[numeric_cols].mean().round(2))

if __name__ == "__main__":
    main()
