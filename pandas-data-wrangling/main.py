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

# remove invalid dates
df = df.dropna()

print(df.to_string())
print(df.info())
print(df.describe())