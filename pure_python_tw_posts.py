import csv
import statistics
from collections import Counter, defaultdict

FILE_PATH = 'C:/Users/Hp/Documents/OPT Research/period_03/2024_tw_posts_president_scored_anon.csv'

def is_float(value):
    try:
        float(value)
        return True
    except:
        return False

def analyze_csv(file_path):
    numeric_columns = ['retweetCount', 'replyCount', 'likeCount', 'quoteCount', 'viewCount', 'bookmarkCount']
    categorical_columns = ['source', 'lang', 'isReply', 'isRetweet', 'isQuote']

    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)

    print("Total Rows:", len(data))

    # --- Numeric Stats ---
    for col in numeric_columns:
        values = [float(row[col]) for row in data if is_float(row[col])]
        if not values:
            continue
        print(f"\n=== Numeric Column: {col} ===")
        print("Count:", len(values))
        print("Mean:", round(statistics.mean(values), 2))
        print("Min:", min(values))
        print("Max:", max(values))
        print("Std Dev:", round(statistics.stdev(values), 2) if len(values) > 1 else "N/A")

    # --- Categorical Stats ---
    for col in categorical_columns:
        freq = Counter(row[col] for row in data)
        print(f"\n=== Categorical Column: {col} ===")
        print("Unique values:", len(freq))
        print("Most common:", freq.most_common(3))

    # --- Group by month_year and average metrics ---
    grouped = defaultdict(list)
    for row in data:
        key = row['month_year']
        if all(is_float(row[col]) for col in numeric_columns):
            grouped[key].append({col: float(row[col]) for col in numeric_columns})

    print("\n=== Grouped by month_year ===")
    for key, group_rows in grouped.items():
        print(f"\nMonth: {key}")
        for col in numeric_columns:
            col_values = [row[col] for row in group_rows]
            if col_values:
                print(f"{col}: avg={round(statistics.mean(col_values), 2)}")

if __name__ == "__main__":
    analyze_csv(FILE_PATH)


