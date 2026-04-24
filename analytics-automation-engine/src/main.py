"""
ENTRY POINT

Orchestrates the full data pipeline:
Load → Clean → Analyze → Report
"""

from data_loader import load_data
from data_management import clean_data, transform_data

df = load_data()
df = clean_data(df)
df = transform_data(df)

print(df.head())