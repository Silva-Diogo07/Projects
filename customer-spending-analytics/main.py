import pandas as pd
from pathlib import Path

script_dir = Path(__file__).parent
dataCSV_path = script_dir / "data" / "customer_order.csv"

df = pd.read_csv(dataCSV_path)

# create total column
df["total"] = df["quantity"] * df["price"]

# sort by country and price
df = df.sort_values(["country", "order_date"])

# group and print
for country, data in df.groupby("country"):
    print(f"\nCountry: {country}")
    print(data.to_string(index=False))
