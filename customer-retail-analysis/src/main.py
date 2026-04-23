from src.data_loader import load_data
from src.analysis import get_extreme_customers, compute_business_metrics
from src.utils import print_customers, print_series


def main():
    # Load data
    df = load_data()

    # -----------------------
    # Top-level preview
    # -----------------------
    df_top5 = df.sort_values(["country", "customer_id"]).groupby("country").head(5)

    print("Top 5 customers per country:")
    print(df_top5)

    # -----------------------
    # Extreme customers
    # -----------------------
    extremes = get_extreme_customers(df)

    print_customers(extremes["youngest"], "Youngest customers by country")
    print_customers(extremes["oldest"], "Oldest customers by country")
    print_customers(extremes["least_spent"], "Lowest spenders", True)
    print_customers(extremes["most_spent"], "Highest spenders", True)

    # -----------------------
    # Business insights
    # -----------------------
    metrics = compute_business_metrics(df)

    print_series("Average spending per country", metrics["avg_spending"])
    print_series("Revenue by channel", metrics["revenue_by_channel"])
    print_series("Customer activity distribution", metrics["activity_distribution"])
    print_series("Conversion rate per country", metrics["conversion_by_country"])


if __name__ == "__main__":
    main()