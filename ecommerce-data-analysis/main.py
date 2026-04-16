import pandas as pd
from pathlib import Path

script_dir = Path(__file__).parent
dataCSV_path = script_dir / "data" / "e-commerce_orders.csv"

# read csv
df = pd.read_csv(dataCSV_path)
print(df)

