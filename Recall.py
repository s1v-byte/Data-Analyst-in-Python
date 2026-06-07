import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

df = pd.read_csv("dirty_cafe_sales.csv")

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
df["price_per_unit"] = pd.to_numeric(df["price_per_unit"], errors="coerce")
df["total_spent"] = pd.to_numeric(df["total_spent"], errors="coerce")
df["transaction_date"] = pd.to_datetime(df["transaction_date"], errors="coerce")

total_spent = df.groupby("item")["total_spent"].sum().sort_values(ascending=False)

total_spent.plot(kind="bar")
plt.title("Total Item Revenue")
plt.xlabel("Item")
plt.ylabel("Revenue")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()


plt.figure(figsize=(6, 4))
sns.countplot(
    data=df,
    x="payment_method"
)
plt.title("Payment Method Usage")
plt.tight_layout()
plt.show()
