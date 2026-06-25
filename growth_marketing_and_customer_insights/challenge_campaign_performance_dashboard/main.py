import pandas as pd

def campaign_performance_dashboard():
    # Hardcoded campaign data
    data = {
        "campaign": ["Spring Launch", "Summer Sale", "Holiday Promo", "Referral Boost"],
        "impressions": [10000, 8000, 15000, 5000],
        "clicks": [500, 400, 900, 300],
        "conversions": [50, 32, 110, 25],
    }
    df = pd.DataFrame(data)

    # Calculate conversion rate for each campaign
    df["conversion_rate"] = df["conversions"] / df["impressions"]

    # Identify the best-performing campaign (highest conversion rate)
    best_campaign_idx = df["conversion_rate"].idxmax()
    best_campaign = df.loc[best_campaign_idx, "campaign"]
    best_rate = df.loc[best_campaign_idx, "conversion_rate"]

    # Prepare summary dashboard
    dashboard = "Campaign Performance Dashboard\n"
    dashboard += "-" * 35 + "\n"
    for _, row in df.iterrows():
        campaign_summary = (
            f"Campaign: {row['campaign']}\n"
            f"  Impressions: {row['impressions']}\n"
            f"  Clicks: {row['clicks']}\n"
            f"  Conversions: {row['conversions']}\n"
            f"  Conversion Rate: {row['conversion_rate']:.2%}\n"
        )
        dashboard += campaign_summary + "\n"
    dashboard += f"Best-Performing Campaign: {best_campaign} ({best_rate:.2%} conversion rate)\n"

    dashboard_output = dashboard
    print(dashboard_output)

campaign_performance_dashboard()
