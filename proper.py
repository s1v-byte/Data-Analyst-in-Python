import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# LOAD DATA
# =========================

df = pd.read_csv("dirty_cafe_sales.csv")

print("\n=== ORIGINAL DATASET ===")
print("Shape:", df.shape)
print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

# =========================
# CLEAN DATA
# =========================

bad_values = ["UNKNOWN", "ERROR"]

columns_to_clean = [
    "Item",
    "Payment Method",
    "Location",
    "Total Spent"
]

for col in columns_to_clean:
    df = df[~df[col].isin(bad_values)]

# Remove rows with missing values in key columns
df = df.dropna(
    subset=[
        "Item",
        "Payment Method",
        "Location",
        "Total Spent"
    ]
)

# Convert data types
df["Quantity"] = pd.to_numeric(
    df["Quantity"],
    errors="coerce"
)

df["Price Per Unit"] = pd.to_numeric(
    df["Price Per Unit"],
    errors="coerce"
)

df["Total Spent"] = pd.to_numeric(
    df["Total Spent"],
    errors="coerce"
)

df["Transaction Date"] = pd.to_datetime(
    df["Transaction Date"],
    errors="coerce"
)

# Remove rows where conversion failed
df = df.dropna(
    subset=[
        "Quantity",
        "Price Per Unit",
        "Total Spent",
        "Transaction Date"
    ]
)

# Remove duplicates
df = df.drop_duplicates()

# Optional business-rule cleaning
df = df[
    (df["Quantity"] > 0) &
    (df["Price Per Unit"] > 0) &
    (df["Total Spent"] > 0)
]

# =========================
# FEATURE ENGINEERING
# =========================

df["Year"] = df["Transaction Date"].dt.year
df["Month"] = df["Transaction Date"].dt.month
df["Month Name"] = df["Transaction Date"].dt.month_name()
df["Day"] = df["Transaction Date"].dt.day_name()

# =========================
# VALIDATION
# =========================

print("\n=== CLEANED DATASET ===")
print("Shape:", df.shape)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# =========================
# DESCRIPTIVE STATISTICS
# =========================

print("\n=== TOTAL SPENT SUMMARY ===")
print(df["Total Spent"].describe())

# =========================
# SALES ANALYSIS
# =========================

print("\n=== ITEM FREQUENCY ===")
print(df["Item"].value_counts())

print("\n=== PAYMENT METHOD FREQUENCY ===")
print(df["Payment Method"].value_counts())

print("\n=== LOCATION FREQUENCY ===")
print(df["Location"].value_counts())

print("\n=== REVENUE BY ITEM ===")
item_sales = (
    df.groupby("Item")["Total Spent"]
      .sum()
      .sort_values(ascending=False)
)
print(item_sales)

print("\n=== REVENUE BY PAYMENT METHOD ===")
payment_sales = (
    df.groupby("Payment Method")["Total Spent"]
      .sum()
      .sort_values(ascending=False)
)
print(payment_sales)

print("\n=== REVENUE BY LOCATION ===")
location_sales = (
    df.groupby("Location")["Total Spent"]
      .sum()
      .sort_values(ascending=False)
)
print(location_sales)

print("\n=== MONTHLY REVENUE ===")
monthly_sales = (
    df.groupby("Month Name")["Total Spent"]
      .sum()
)
print(monthly_sales)

# =========================
# VISUALIZATIONS
# =========================

sns.set_style("whitegrid")

# Revenue by Item
plt.figure(figsize=(10, 5))
item_sales.plot(kind="bar")
plt.title("Revenue by Item")
plt.xlabel("Item")
plt.ylabel("Total Revenue")
plt.tight_layout()
plt.show()

# Revenue by Location
plt.figure(figsize=(8, 5))
location_sales.plot(kind="bar", color="orange")
plt.title("Revenue by Location")
plt.xlabel("Location")
plt.ylabel("Total Revenue")
plt.tight_layout()
plt.show()

# Payment Method Distribution
plt.figure(figsize=(6, 4))
sns.countplot(
    data=df,
    x="Payment Method"
)
plt.title("Payment Method Usage")
plt.tight_layout()
plt.show()

# Distribution of Total Spent
plt.figure(figsize=(8, 5))
sns.histplot(
    df["Total Spent"],
    bins=20,
    kde=True
)
plt.title("Distribution of Total Spent")
plt.xlabel("Amount")
plt.tight_layout()
plt.show()

# Monthly Revenue Trend
monthly_trend = (
    df.groupby("Month")["Total Spent"]
      .sum()
)

plt.figure(figsize=(8, 5))
monthly_trend.plot(
    marker="o",
    linewidth=2
)
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True)
plt.tight_layout()
plt.show()

print("\n=== BUSINESS INSIGHTS ===")
print("Top Selling Item:")
print(item_sales.idxmax())

print("\nHighest Revenue Location:")
print(location_sales.idxmax())

print("\nMost Used Payment Method:")
print(df["Payment Method"].value_counts().idxmax())

print(df.shape)