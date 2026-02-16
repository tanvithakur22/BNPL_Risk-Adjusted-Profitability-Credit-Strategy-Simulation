import pandas as pd
import numpy as np

np.random.seed(42)

NUM_USERS = 50000

data = []

for i in range(NUM_USERS):
    
    user_id = f"BNPL_{i+1:06d}"
    
    age = np.random.randint(21, 55)
    income = np.random.randint(15000, 120000)
    
    credit_score = np.random.randint(300, 850)
    
    # Loan logic
    loan_amount = np.random.randint(2000, 30000)
    tenure_months = 3
    
    interest_rate = 0.18  # 18% annualized
    merchant_commission_rate = 0.03
    acquisition_cost = np.random.randint(200, 600)
    
    # Default probability based on credit score
    if credit_score >= 750:
        default_prob = 0.02
    elif credit_score >= 650:
        default_prob = 0.06
    elif credit_score >= 550:
        default_prob = 0.12
    else:
        default_prob = 0.25
        
    defaulted = np.random.choice([1, 0], p=[default_prob, 1-default_prob])
    
    # Revenue
    interest_income = loan_amount * interest_rate * (tenure_months / 12)
    merchant_income = loan_amount * merchant_commission_rate
    
    revenue = interest_income + merchant_income
    
    # Loss
    loss = loan_amount if defaulted == 1 else 0
    
    # Net Profit
    net_profit = revenue - loss - acquisition_cost
    
    data.append([
        user_id,
        age,
        income,
        credit_score,
        loan_amount,
        tenure_months,
        interest_rate,
        merchant_commission_rate,
        acquisition_cost,
        defaulted,
        round(revenue,2),
        round(loss,2),
        round(net_profit,2)
    ])

columns = [
    "user_id",
    "age",
    "income",
    "credit_score",
    "loan_amount",
    "tenure_months",
    "interest_rate",
    "merchant_commission_rate",
    "acquisition_cost",
    "defaulted",
    "revenue",
    "loss",
    "net_profit"
]

df = pd.DataFrame(data, columns=columns)

df.to_csv("bnpl_portfolio_dataset.csv", index=False)

print("BNPL synthetic dataset generated successfully.")
