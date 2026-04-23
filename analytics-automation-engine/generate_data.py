"""
=========================================================
📊 SYNTHETIC SALES DATA GENERATOR
=========================================================

⚠️ IMPORTANT TRANSPARENCY NOTICE:

This dataset is FULLY SYNTHETIC and AI-GENERATED.

Purpose:
- Created for learning, portfolio, and data engineering practice
- Simulates realistic e-commerce sales behavior
- NOT based on real customers, transactions, or companies

Why this exists:
- Practice ETL pipelines (Extract, Transform, Load)
- Build analytics dashboards and reports
- Train data cleaning and transformation workflows

Data characteristics:
- Includes seasonality effects (e.g., Black Friday, Christmas)
- Product-based pricing logic
- Country-based behavior variation
- Realistic sales distribution patterns

=========================================================
"""

import pandas as pd
import numpy as np
from pathlib import Path
import random
from datetime import datetime

# -----------------------------
# CONFIG
# -----------------------------
output_dir = Path("data")
output_dir.mkdir(exist_ok=True)

months = [
    "jan", "feb", "mar", "apr", "may", "jun",
    "jul", "aug", "sep", "oct", "nov", "dec"
]

products = [
    ("Shoes", "Fashion"),
    ("T-Shirt", "Fashion"),
    ("Watch", "Accessories"),
    ("Bag", "Accessories"),
    ("Headphones", "Electronics"),
    ("Phone Case", "Electronics")
]

countries = ["Portugal", "Spain", "France", "Germany", "Italy"]

channels = ["Google Ads", "Instagram", "TikTok", "Email", "Organic"]

# -----------------------------
# SEASONALITY MODEL
# -----------------------------
seasonality_factor = {
    "jan": 0.8,
    "feb": 0.75,
    "mar": 0.85,
    "apr": 0.9,
    "may": 1.0,
    "jun": 1.1,
    "jul": 1.3,
    "aug": 1.4,
    "sep": 1.05,
    "oct": 1.0,
    "nov": 1.6,   # Black Friday
    "dec": 1.8    # Christmas peak
}

# -----------------------------
# PRODUCT PRICE RANGES
# -----------------------------
price_map = {
    "Shoes": (40, 120),
    "T-Shirt": (10, 40),
    "Watch": (80, 300),
    "Bag": (30, 150),
    "Headphones": (50, 200),
    "Phone Case": (10, 30)
}

# -----------------------------
# COUNTRY BEHAVIOR MODEL
# -----------------------------
country_multiplier = {
    "Portugal": 0.9,
    "Spain": 1.0,
    "France": 1.1,
    "Germany": 1.3,
    "Italy": 1.0
}

# -----------------------------
# GENERATE MONTH DATA
# -----------------------------
def generate_month_data(month, base_rows=200):
    data = []

    factor = seasonality_factor[month]
    total_rows = int(base_rows * factor)

    for i in range(total_rows):

        product, category = random.choice(products)

        # price based on product type
        min_p, max_p = price_map[product]
        price = round(np.random.uniform(min_p, max_p), 2)

        # country behavior impact
        country = random.choice(countries)
        multiplier = country_multiplier[country]

        # realistic quantity (skewed distribution)
        quantity = max(1, int(np.random.poisson(2) * multiplier))

        row = {
            "order_id": f"{month.upper()}_{i+1}",
            "date": f"2024-{str(months.index(month)+1).zfill(2)}-{np.random.randint(1,28)}",
            "product": product,
            "category": category,
            "country": country,
            "quantity": quantity,
            "price": price,
            "revenue": round(quantity * price, 2),
            "channel": random.choice(channels)
        }

        data.append(row)

    return pd.DataFrame(data)

# -----------------------------
# GENERATE ALL MONTHS
# -----------------------------
for month in months:
    df = generate_month_data(month)

    file_path = output_dir / f"sales_{month}.csv"
    df.to_csv(file_path, index=False)

    print(f"Generated: {file_path} ({len(df)} rows)")

# -----------------------------
# METADATA FILE
# -----------------------------
meta = {
    "generated_by": "AI-assisted Python script",
    "purpose": "Synthetic dataset for data pipeline & analytics practice",
    "data_type": "Fully artificial sales simulation",
    "features": "Seasonality, pricing logic, country behavior, revenue column",
    "created_at": datetime.now().isoformat(),
    "warning": "This data does NOT represent real-world users or transactions"
}

meta_path = output_dir / "DATASET_INFO.txt"

with open(meta_path, "w", encoding="utf-8") as f:
    for k, v in meta.items():
        f.write(f"{k}: {v}\n")

print("\n✅ Dataset generation completed successfully.")
print("⚠️ All data is synthetic and AI-generated for learning purposes.")