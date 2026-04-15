import pandas as pd
from pathlib import Path

script_dir = Path(__file__).parent
dataCSV_path = script_dir / "data" / "sales_data.csv"

df = pd.DataFrame(dataCSV_path)
print(df)