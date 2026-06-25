import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def visualize_customer_segments():
    data = {
        "age": [25, 32, 45, 28, 39, 50, 22, 41, 36, 29, 48, 27],
        "segment": [
            "Startup", "Enterprise", "Startup", "Enterprise",
            "Startup", "Enterprise", "Startup", "Enterprise",
            "Startup", "Enterprise", "Startup", "Enterprise"
        ],
        "monthly_spend": [120, 350, 200, 400, 180, 420, 90, 390, 210, 370, 130, 410]
    }
    df = pd.DataFrame(data)
    plt.figure(figsize=(8,5))
    ax = sns.boxplot(data=df, x="segment", y= "monthly_spend")
    ax.set_title("Monthly Spend by Customer Segment")
    ax.set_xlabel("Customer Segment")
    ax.set_ylabel("Monthly Spend ($)")
    plt.tight_layout()
    plt.show()
    insight = "Enterprise customers show consistently higher monthly spend compared to Startup customers, with less variation in spending."
    print(insight)

visualize_customer_segments()