import csv
import statistics
from collections import defaultdict, Counter

FILE_PATH = 'C:/Users/Hp/Documents/OPT Research/period_03/2024_fb_ads_president_scored_anon.csv' 

def is_float(val):
    try:
        float(val.replace(",", "").strip())
        return True
    except:
        return False

def to_float(val):
    return float(val.replace(",", "").strip()) if is_float(val) else 0.0

def analyze_csv(file_path):
    numeric_cols = [
        'estimated_audience_size',
        'estimated_impressions',
        'estimated_spend'
    ]

    categorical_cols = ['currency', 'publisher_platforms']

    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)

    print("Total rows:", len(data))

    # --- Numeric Stats ---
    for col in numeric_cols:
        values = [to_float(row[col]) for row in data if row[col].strip()]
        if values:
            print(f"\n=== Numeric Column: {col} ===")
            print("Count:", len(values))
            print("Mean:", round(statistics.mean(values), 2))
            print("Min:", min(values))
            print("Max:", max(values))
            if len(values) > 1:
                print("Std Dev:", round(statistics.stdev(values), 2))

    # --- Categorical Stats ---
    for col in categorical_cols:
        counts = Counter(row[col] for row in data if row[col].strip())
        print(f"\n=== Categorical Column: {col} ===")
        print("Unique values:", len(counts))
        print("Most common:", counts.most_common(3))

    # --- Group by page_id ---
    grouped = defaultdict(list)
    for row in data:
        key = row['page_id']
        if all(is_float(row[col]) for col in numeric_cols):
            grouped[key].append({col: to_float(row[col]) for col in numeric_cols})

    print("\n=== Grouped by page_id (mean values) ===")
    for page, rows in grouped.items():
        print(f"\nPage ID: {page}")
        for col in numeric_cols:
            col_values = [r[col] for r in rows]
            if col_values:
                print(f"{col}: avg={round(statistics.mean(col_values), 2)}")

if __name__ == "__main__":
    analyze_csv(FILE_PATH)
