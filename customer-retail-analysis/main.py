import pandas as pd
from pathlib import Path

script_dir = Path(__file__).parent
dataCSV_path = script_dir / "data" / "retail_customer_data.csv"

df = pd.read_csv(dataCSV_path)

# Sort df by country and id, then orders by country and shows first 5
df = df.sort_values(by=["country", "customer_id"]).groupby("country").head(5)

print(df)

# finds the youngest customer
youngest_customers = df.loc[df.groupby("country")["age"].idxmin()]
print("\nYoungest customers by country:")
for _, row in youngest_customers.iterrows():
    print(f"From {row['country']} is the customer {row['customer_id']} with the age of {row['age']} ")

# finds the oldest customer
oldest_customer = df.loc[df.groupby("country")["age"].idxmax()]
print("\nOldest customer by country:")
for _, row in oldest_customer.iterrows():
    print(f"From {row['country']} is the customer {row['customer_id']} with the age of {row['age']} ")
