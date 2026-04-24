"""
LOAD DATA

Responsible for:
- Reading all CSV files from the data folder
- Combining them into a single DataFrame
- Adding basic metadata (source file)
"""

from pathlib import Path
import pandas as pd
import logging


# INFO level = show normal execution messages (not too verbose, not too silent)
# Format includes timestamp, log level, and message
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def load_data() -> pd.DataFrame:
    """
    Load and combine all CSV files from the data directory.

    Returns:
        pd.DataFrame: A single DataFrame containing all rows from all files
    """

    # resolve() = get absolute path
    base_dir = Path(__file__).resolve().parent.parent

    data_path = base_dir / "data"

    # Check if the folder exists before trying to read files
    if not data_path.exists():
        logging.error(f"Data folder not found: {data_path}")
        raise FileNotFoundError(f"Missing folder: {data_path}")

    # Find all CSV files inside the data folder
    # "*.csv" = match every file ending in .csv
    # sorted() ensures consistent order every time the code runs
    files = sorted(data_path.glob("*.csv"))

    # If no files are found, stop execution early
    if not files:
        logging.error("No CSV files found in data folder")
        raise ValueError("No data files to load")

    logging.info(f"Found {len(files)} CSV files")

    df_list = []

    # Loop through each file and read it into a DataFrame
    for file in files:
        try:
            logging.info(f"Reading file: {file.name}")

            # Read CSV into pandas DataFrame
            df = pd.read_csv(file)

            # Add a new column to track where each row came from
            # file.stem = filename without extension (e.g., "january")
            df["source_file"] = file.stem

            # Store DataFrame in list for later combination
            df_list.append(df)

        except Exception as e:
            # If something goes wrong, log the error and stop execution
            logging.error(f"Error reading {file.name}: {e}")
            raise

    # Combine all DataFrames into one
    # ignore_index=True = reset index (avoid duplicate indices)
    df_final = pd.concat(df_list, ignore_index=True)

    logging.info(f"Final dataset shape: {df_final.shape}")

    return df_final