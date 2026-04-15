import pandas as pd
from pathlib import Path

script_dir = Path(__file__).parent
main_dir = script_dir.parent    
dataCSV_path = main_dir / "data" / "sales_data.csv"

df = pd.DataFrame(dataCSV_path)
print(df)