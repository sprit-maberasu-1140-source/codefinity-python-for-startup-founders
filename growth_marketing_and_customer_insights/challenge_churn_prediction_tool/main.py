import pandas as pd
from sklearn.linear_model import LogisticRegression

# Hardcoded customer data for training
data = {
    "account_age_months": [12, 4, 24, 36, 8, 18, 6, 30],
    "monthly_usage": [50, 10, 60, 70, 20, 40, 15, 65],
    "num_support_tickets": [1, 5, 0, 2, 3, 1, 4, 0],
    "churned": [0, 1, 0, 0, 1, 0, 1, 0]
}
df = pd.DataFrame(data)

# Features and label
X = df[["account_age_months", "monthly_usage", "num_support_tickets"]]
y = df["churned"]

# Train logistic regression model
model = LogisticRegression()
model.fit(X, y)

# New customer data for prediction
new_customers = pd.DataFrame({
    "account_age_months": [5, 20, 10],
    "monthly_usage": [12, 55, 25],
    "num_support_tickets": [4, 0, 2]
})

# Predict churn for new customers
predictions = model.predict(new_customers)
print("Churn predictions for new customers:", predictions)

# Summarize feature importance
feature_names = X.columns
coefficients = model.coef_[0]
feature_importance = pd.Series(coefficients, index=feature_names).abs().sort_values(ascending=False)
print("Feature importance for churn prediction:")
print(feature_importance)
