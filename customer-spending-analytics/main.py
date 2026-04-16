import pandas as pd
from pathlib import Path

script_dir = Path(__file__).parent
dataCSV_path = script_dir / "data" / "customer_order.csv"

df = pd.read_csv(dataCSV_path)

# create a new 'total' column
df["total"] = df["quantity"] * df["price"]

# order by country and price
df_sorted = df.sort_values(["country", "price"], ascending=[True, True])

print(df_sorted)

# clean e structure the dataset for analyse
# create a new 'total' column
# identify the client that spends the most and his country
# number of purchases by each client
