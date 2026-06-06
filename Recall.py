import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dirty_cafe_sales.csv")

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Convert data types
df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
df["transaction_date"] = pd.to_datetime(df["transaction_date"], errors="coerce")

# Visualization
item_sales = df.groupby("item")["quantity"].sum()

"""item_sales.plot(kind="bar")
plt.title("Total Item Quantity Sold")
plt.xlabel("Item")
plt.ylabel("Quantity")
plt.tight_layout()
plt.show()"""

print(df.shape)