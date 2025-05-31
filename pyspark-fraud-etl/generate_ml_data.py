import pandas as pd
import numpy as np


np.random.seed(42)
n = 1000

data = {
    "amount": np.random.exponential(scale=200, size=n),
    "is_foreign": np.random.binomial(1, 0.1, n),
    "is_high_risk_country": np.random.binomial(1, 0.05, n),
    "hour": np.random.randint(0, 24, n),
    "day_of_week": np.random.randint(1, 8, n),
}

data["rule_fraud"] = (
    (data["amount"] > 300) |
    (np.array(data["is_foreign"]) & np.array(data["is_high_risk_country"]))
).astype(int)

data["ml_fraud"] = (
    (data["amount"] > 500) |
    ((np.array(data["is_foreign"]) == 1) & (np.random.rand(n) > 0.5))
).astype(int)

df = pd.DataFrame(data)
df.to_csv("transactions.csv", index=False)
print("transactions.csv saved.")