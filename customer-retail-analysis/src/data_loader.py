from pathlib import Path
import pandas as pd


def load_data():
    """
    Loads the retail customer dataset from the data folder.
    Keeps path logic centralized to avoid duplication.
    """
    script_dir = Path(__file__).resolve().parent.parent
    data_path = script_dir / "data" / "retail_customer_data.csv"

    return pd.read_csv(data_path, encoding="utf-8")