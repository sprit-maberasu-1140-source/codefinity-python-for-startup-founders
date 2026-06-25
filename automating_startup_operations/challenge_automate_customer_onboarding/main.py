def generate_onboarding_message(name):
    message = f"Welcome, {name}! We're excited to have you onboard. Your journey with us starts now."
    return message

def onboard_customers(customers):
    onboarded = []
    for customer in customers:
        name = customer["name"]
        email = customer["email"]
        message = generate_onboarding_message(name)
        status = "Onboarded"
        onboarded.append({"name": name, "email": email, "onboarding_status": status, "message": message})
    return onboarded

# Hardcoded list of new customers
new_customers = [
    {"name": "Alice Johnson", "email": "alice.johnson@example.com"},
    {"name": "Bob Smith", "email": "bob.smith@example.com"},
    {"name": "Charlie Lee", "email": "charlie.lee@example.com"},
]

onboarded_customers = onboard_customers(new_customers)

for customer in onboarded_customers:
    summary = f"Name: {customer['name']}, Email: {customer['email']}, Status: {customer['onboarding_status']}"
    print(summary)
