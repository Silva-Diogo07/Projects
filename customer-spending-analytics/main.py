import pandas as pd
from pathlib import Path

script_dir = Path(__file__).parent
dataCSV_path = script_dir / "data" / "customer_order.csv"
df = pd.read_csv(dataCSV_path)

# create total column
df["total"] = df["quantity"] * df["price"]

# sort by country and price
df = df.sort_values(["country", "order_date"])

# orders the data by country
# for each country shows it's data
for country, data in df.groupby("country"):
    print(f"\nCountry: {country}") 
    print(data.to_string(index=False))

# orders by client
# sum all expenses for each customer
total_by_customer = df.groupby("customer_id")["total"].sum()
# finds the client that spent the most
top_customer = total_by_customer.idxmax()
# returns the most spent value
top_value = total_by_customer.max()
# filters by customer_id , picks the column 'country' and picks the first value
top_country = df[df["customer_id"] == top_customer]["country"].iloc[0]

print(f"Top customer: {top_customer}\nTotal spent: {top_value:,.2f}€\nCustomer country: {top_country}")
