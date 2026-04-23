
def print_customers(df, title, show_spending=False):
    """
    Pretty prints customer analysis results.
    Focused only on presentation (no logic here).
    """
    print(f"\n{title}")

    for row in df.itertuples():
        if not show_spending:
            print(f"{row.country} → {row.customer_id} | Age {row.age}")
        else:
            print(
                f"{row.country} → {row.customer_id} | "
                f"{row.purchases} purchases | {row.total_spent}£"
            )


def print_series(title, series):
    """
    Prints pandas Series in a consistent format.
    """
    print(f"\n{title}")
    print(series)