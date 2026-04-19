import pandas as pd
from pathlib import Path

script_dir = Path(__file__).parent
dataCSV_path = script_dir / "data" / "customer_order.csv"
df = pd.read_csv(dataCSV_path)

# create a new "total" representing the total value per order line
# (quantity * unit price)
df["total"] = df["quantity"] * df["price"]

# Sort the dataset by country and order date
# This helps organize the data for chronological analysis within each country
df = df.sort_values(["country", "order_date"])

# Group the data by country and print each group separately
# This allows an easy inspection of all orders per country
for country, data in df.groupby("country"):
    print(f"\nCountry: {country}") 
    print(data.to_string(index=False))

# Group data by customer and calculate the total amount spent per customer
total_by_customer = df.groupby("customer_id")["total"].sum()
# Identify the customer who spent the most
top_customer = total_by_customer.idxmax()
# Get the total amount spent by that customer
top_value = total_by_customer.max()
# Retrieve the country of the top customer
# (assumes each customer belongs to a single country)
top_country = df[df["customer_id"] == top_customer]["country"].iloc[0]

# Calculate total sales per country
total_by_country = df.groupby("country")["total"].sum()
# Remove the index name for cleaner output formatting
total_by_country.index.name = None
# Format the totals as currency (euros with two decimal places)
total_by_country_formatted = total_by_country.apply(lambda x: f"{x:,.2f}€")

# Print information about the highest-spending customer
print(
    f"Top customer id: {top_customer}\n"
    f"Total spent: {top_value:,.2f}€\n"
    f"Customer country: {top_country}"
)

# Print total sales by country
print("\nTotal by country:")
print(total_by_country_formatted)
