import pandas as pd
from pathlib import Path

script_dir = Path(__file__).parent  
dataCSV_path = script_dir / "data" / "sales_data.csv"

df = pd.read_csv(dataCSV_path)

# convert dates properly
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# limit Duration
df.loc[df["Duration"] > 120, "Duration"] = 120

# remove duplicates
df = df.drop_duplicates()

# remove invalid values
df = df.dropna()

# reset index (for cleaner output)
df = df.reset_index(drop=True)

# Data Exploration

print("\n--- CLEAN DATA ---\n")
print(df.to_string())

print("\n--- INFO ---\n")
print(df.info())

print("\n--- DESCRIBE ---\n")
print(df.describe())

print("\n--- MEAN BY CATEGORY ---\n")
print(df.groupby("Category")[["Price", "Duration"]].mean())

print("\n--- VALUE COUNTS (Category) ---\n")
print(df["Category"].value_counts())

print("\n--- MOST EXPENSIVE PRODUCT ---\n")
print(df.loc[df["Price"].idxmax()])

print("\n--- CORRELATION ---\n")
print(df[["Duration", "Price"]].corr())