import pandas as pd
from pathlib import Path


def get_extreme_by_group(df, group_col, target_col, func):
    """
    Returns rows with the minimum or maximum value of a column within each group.

    Example:
        - Youngest customer per country
        - Highest spender per country
    """
    idx = getattr(df.groupby(group_col)[target_col], func)()
    return df.loc[idx]


def print_customers(df, title, show_spending=False):
    """
    Prints customer information in a readable format.

    Parameters:
        df (DataFrame): Data to print
        title (str): Section title
        show_spending (bool): If True, shows purchases and total spent.
    """
    print(f"\n{title}")

    for row in df.itertuples():

        # Basic output (e.g. age-based analysis)
        if not show_spending:
            print(f"{row.country} → {row.customer_id} | Age {row.age}")

        # Detailed output (e.g. spending analysis)
        else:
            print(
                f"{row.country} → {row.customer_id} | "
                f"{row.purchases} purchases | {row.total_spent}£"
            )


# -----------------------------
# Load dataset
# -----------------------------
script_dir = Path(__file__).parent
dataCSV_path = script_dir / "data" / "retail_customer_data.csv"

df = pd.read_csv(dataCSV_path, encoding="utf-8")


# -----------------------------
# Preview data: top 5 customers per country
# -----------------------------
df_top5 = (
    df.sort_values(by=["country", "customer_id"])
      .groupby("country")
      .head(5)
)

print("Top 5 customers per country:")
print(df_top5)


# -----------------------------
# Identify extreme values per country
# -----------------------------
youngest = get_extreme_by_group(df, "country", "age", "idxmin")
oldest = get_extreme_by_group(df, "country", "age", "idxmax")

least_spent = get_extreme_by_group(df, "country", "total_spent", "idxmin")
most_spent = get_extreme_by_group(df, "country", "total_spent", "idxmax")


# -----------------------------
# Display results
# -----------------------------
print_customers(youngest, "Youngest customers by country")
print_customers(oldest, "Oldest customers by country")

print_customers(
    least_spent,
    "Customers with lowest spending by country",
    show_spending=True
)

print_customers(
    most_spent,
    "Customers with highest spending by country",
    show_spending=True
)


# -----------------------------
# Basic business insights
# -----------------------------

# Average revenue per country
print("\nAverage spending per country:")
print(df.groupby("country")["total_spent"].mean().sort_values(ascending=False))

# Total revenue per marketing channel
print("\nRevenue by acquisition channel:")
print(df.groupby("acquisition_channel")["total_spent"].sum().sort_values(ascending=False))

# Customer activity distribution (active vs inactive)
print("\nCustomer activity distribution:")
print(df["is_active"].value_counts())

# Conversion rate (purchases per product views)
df["conversion_rate"] = df["purchases"] / df["product_views"]

print("\nAverage conversion rate per country:")
print(df.groupby("country")["conversion_rate"].mean().sort_values(ascending=False))