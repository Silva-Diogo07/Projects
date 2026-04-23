import pandas as pd
from pathlib import Path

script_dir = Path(__file__).parent
dataCSV_path = script_dir / "data" / "retail_customer_data.csv"

df = pd.read_csv(dataCSV_path)

# Sort df by country and id, then orders by country and shows first 5
df = df.sort_values(by=["country", "customer_id"]).groupby("country").head(5)

print(df)

# finds the youngest customer in each country
youngest_customers = df.loc[df.groupby("country")["age"].idxmin()]
print("\nYoungest customers by country:")
for _, row in youngest_customers.iterrows():
    print(f"From {row['country']} is the customer {row['customer_id']} with the age of {row['age']} ")

# finds the oldest customer in each country
oldest_customers = df.loc[df.groupby("country")["age"].idxmax()]
print("\nOldest customer by country:")
for _, row in oldest_customers.iterrows():
    print(f"From {row['country']} is the customer {row['customer_id']} with the age of {row['age']} ")

# finds the customers that spent the least in each country
least_spent_customer = df.loc[df.groupby("country")["total_spent"].idxmin()]
print("\nCustomers that spent the least:")
for _, row in least_spent_customer.iterrows():
    print(f"From {row['country']} is the customer {row['customer_id']} with {row['purchases']} purchases with a total of {row['total_spent']}£ spent")

# finds the customers that spent the most in each country
top_spent_customers = df.loc[df.groupby("country")["total_spent"].idxmax()]
print("\nCustomers that spent the most:")
for _, row in top_spent_customers.iterrows():
    print(f"From {row['country']} is the customer {row['customer_id']} with {row['purchases']} purchases with a total of {row['total_spent']}£ spent")
