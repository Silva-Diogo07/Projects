import pandas as pd
from pathlib import Path


def get_extreme_by_group(df, group_col, target_col, func):
    """
    Return rows with extreme values (min or max) for a given column within each group.

    Parameters:
        df (DataFrame): Input dataset
        group_col (str): Column to group by (e.g., 'country')
        target_col (str): Column to evaluate (e.g., 'age', 'total_spent')
        func (str): Function name ('idxmin' or 'idxmax')

    Returns:
        DataFrame: Rows corresponding to the extreme values per group
    """
    idx = getattr(df.groupby(group_col)[target_col], func)()
    return df.loc[idx]


# Resolve path to CSV file relative to script location
script_dir = Path(__file__).parent
dataCSV_path = script_dir / "data" / "retail_customer_data.csv"

# Load dataset
df = pd.read_csv(dataCSV_path, encoding="utf-8")

# -----------------------------
# Preview: first 5 customers per country (sorted)
# -----------------------------
df_top5 = (
    df.sort_values(by=["country", "customer_id"])
      .groupby("country")
      .head(5)
)

print("Top 5 customers per country:")
print(df_top5)

# -----------------------------
# Analytical queries (use full dataset, not truncated one)
# -----------------------------

# Youngest customers per country
youngest_customers = get_extreme_by_group(df, "country", "age", "idxmin")

# Oldest customers per country
oldest_customers = get_extreme_by_group(df, "country", "age", "idxmax")

# Customers who spent the least per country
least_spent_customers = get_extreme_by_group(df, "country", "total_spent", "idxmin")

# Customers who spent the most per country
top_spent_customers = get_extreme_by_group(df, "country", "total_spent", "idxmax")

# -----------------------------
# Output results
# -----------------------------

print("\nYoungest customers by country:")
for row in youngest_customers.itertuples():
    print(f"From {row.country}: Customer {row.customer_id}, Age {row.age}")

print("\nOldest customers by country:")
for row in oldest_customers.itertuples():
    print(f"From {row.country}: Customer {row.customer_id}, Age {row.age}")

print("\nCustomers who spent the least:")
for row in least_spent_customers.itertuples():
    print(
        f"From {row.country}: Customer {row.customer_id}, "
        f"{row.purchases} purchases, Total {row.total_spent}£"
    )

print("\nCustomers who spent the most:")
for row in top_spent_customers.itertuples():
    print(
        f"From {row.country}: Customer {row.customer_id}, "
        f"{row.purchases} purchases, Total {row.total_spent}£"
    )