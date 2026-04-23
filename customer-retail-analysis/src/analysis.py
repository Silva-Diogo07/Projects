import pandas as pd


def get_extreme_by_group(df, group_col, target_col, func):
    """
    Returns rows corresponding to min or max values per group.
    Used for identifying extreme customer profiles.
    """
    idx = getattr(df.groupby(group_col)[target_col], func)()
    return df.loc[idx]


def compute_business_metrics(df):
    """
    Computes derived KPIs and aggregated insights.
    Returns multiple summary tables.
    """

    avg_spending = df.groupby("country")["total_spent"].mean().sort_values(ascending=False)

    revenue_by_channel = (
        df.groupby("acquisition_channel")["total_spent"]
        .sum()
        .sort_values(ascending=False)
    )

    activity_distribution = df["is_active"].value_counts()

    df = df.copy()
    df["conversion_rate"] = df["purchases"] / df["product_views"]

    conversion_by_country = (
        df.groupby("country")["conversion_rate"]
        .mean()
        .sort_values(ascending=False)
    )

    return {
        "avg_spending": avg_spending,
        "revenue_by_channel": revenue_by_channel,
        "activity_distribution": activity_distribution,
        "conversion_by_country": conversion_by_country,
    }


def get_extreme_customers(df):
    """
    Returns key customer segments per country.
    """

    return {
        "youngest": get_extreme_by_group(df, "country", "age", "idxmin"),
        "oldest": get_extreme_by_group(df, "country", "age", "idxmax"),
        "least_spent": get_extreme_by_group(df, "country", "total_spent", "idxmin"),
        "most_spent": get_extreme_by_group(df, "country", "total_spent", "idxmax"),
    }