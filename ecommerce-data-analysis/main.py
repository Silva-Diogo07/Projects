import pandas as pd
from pathlib import Path

script_dir = Path(__file__).parent
dataCSV_path = script_dir / "data" / "e-commerce_orders.csv"

# read csv
df = pd.read_csv(dataCSV_path)
df = df.drop_duplicates()

# new 'total' column

df["total"] = df["quantity"] * df["price"]

# order by country and price
df_sorted = df.sort_values(["country", "price"], ascending=[True, True])

# Total by country and cleaner output
totals = df.groupby("country")["total"].sum().reset_index()

print(df_sorted)
print("\nTotal by country:")
print(totals)
