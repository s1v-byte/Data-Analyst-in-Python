import pandas as pd

# Load your Excel file
df = pd.read_excel("cars_with_dummies.xlsx")

# Create dummy variables as 1/0 integers
df_dummies = pd.get_dummies(df, columns=["market_segment"], prefix="market", dtype=int)

# Save back to Excel
df_dummies.to_excel("cars_with_dummies.xlsx", index=False)