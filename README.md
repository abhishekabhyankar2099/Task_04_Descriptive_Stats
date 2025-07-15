# Task 04: Descriptive Statistics of Social Media Activity – iSchool OPT Research

## 📋 Overview
This project analyzes social media activity by political candidates during the 2024 U.S. Presidential Election using three datasets:
- Twitter posts
- Facebook posts
- Facebook ads

Each dataset was processed using:
- Pure Python (no external libraries)
- Pandas
- Polars

## 🧰 Tools Used
- Python 3.11
- `pandas` for DataFrame operations
- `polars` for fast data processing
- Built-in modules: `csv`, `statistics`, `collections`

## 📊 What Each Script Does

Each script:
- Loads and cleans the dataset
- Computes descriptive statistics on numeric and categorical columns
- Groups records by meaningful keys (like `page_id`, `post_created_date`, etc.)
- Outputs summary to the console

  ## 🔍 Summary of Findings

Each method computes:
- Basic statistics (count, mean, min, max, std) for numeric columns like likes, retweets, impressions, and spend.
- Categorical value counts (e.g., post type, source, page category).
- Grouped statistics by `page_id` and other relevant keys like `ad_id`, `post_id`, and `month`.

No major discrepancies were found across platforms. However:
- `Polars` was significantly faster and more memory-efficient on larger CSVs.
- `Pandas` offered the most flexibility for quick inspection and aggregation.
- `Pure Python` gave foundational control but was more verbose and slower for grouping.

---

## 📚 Lessons Learned

- **Polars** is excellent for performance-heavy batch tasks and grouping.
- **Pandas** remains the best tool for one-off data exploration due to intuitive syntax.
- Handling **comma-formatted numerics** is crucial when working with scraped or exported data.
- Properly structuring projects into reusable scripts made it easy to iterate and extend.
- Grouping by compound keys like `(page_id, ad_id)` helped surface unique ad-level insights.

## 📝 Author

Abhishek Abhyankar  
Syracuse University – iSchool OPT Research

## Note
Before running the scripts, be sure to edit the file path(s) accordingly to point to the correct location of your dataset files on your system.



---

Thank you for reviewing this submission!
