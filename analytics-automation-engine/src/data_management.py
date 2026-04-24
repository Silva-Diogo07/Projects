"""
CLEAN DATA

Responsible for:
- Fixing data types
- Handling missing values
- Creating new features
"""

def clean_data(df):

    # remove duplicates
    df = df.drop_duplicates()
    # remove rows where essential fields (date, product, quantity, price) are missing
    df = df.dropna(subset=["date", "product", "quantity", "price"])
    # new column to verify if the data has been cleaned
    df["cleaned"] = True

    return df

def transform_data(df):
    
    # calculate profit as 50% of item price multiplied by quantity sold
    df["profit"] = df["quantity"] * (df["price"] * 0.5)

    return df

