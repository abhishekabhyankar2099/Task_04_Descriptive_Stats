import csv
import statistics
from collections import Counter, defaultdict
from datetime import datetime

FILE_PATH = 'C:/Users/Hp/Documents/OPT Research/period_03/2024_fb_posts_president_scored_anon.csv'  

def is_float(value):
    try:
        float(value.replace(",", ""))  # Handle numbers with commas
        return True
    except:
        return False

def to_float(value):
    return float(value.replace(",", "")) if is_float(value) else 0.0

def analyze_csv(file_path):
    numeric_cols = [
        'Total Interactions', 'Likes', 'Comments', 'Shares',
        'Love', 'Wow', 'Haha', 'Sad', 'Angry', 'Care',
        'Post Views', 'Total Views', 'Total Views For All Crossposts',
        'Overperforming Score'
    ]

    categorical_cols = ['Page Category', 'Type', 'Is Video Owner?']

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

    # --- Group by Page Category and Average Metrics ---
    grouped = defaultdict(list)
    for row in data:
        key = row['Page Category']
        if all(is_float(row[col]) for col in numeric_cols):
            grouped[key].append({col: to_float(row[col]) for col in numeric_cols})

    print("\n=== Grouped by Page Category (mean values) ===")
    for category, rows in grouped.items():
        print(f"\nPage Category: {category}")
        for col in numeric_cols:
            values = [r[col] for r in rows]
            if values:
                print(f"{col}: avg={round(statistics.mean(values), 2)}")

if __name__ == "__main__":
    analyze_csv(FILE_PATH)
