import pandas as pd
import numpy as np

# =========================
# 1. LOAD DATA
# =========================
df = pd.read_csv("dirty_cafe_sales.csv")

# =========================
# 2. STANDARDIZE MISSING VALUES
# =========================
df = df.replace(["UNKNOWN", "ERROR", ""], np.nan)

# =========================
# 3. CLEAN COLUMN NAMES (optional but good practice)
# =========================
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Columns now:
# transaction_id, item, quantity, price_per_unit, total_spent, payment_method, location, transaction_date

# =========================
# 4. CONVERT DATA TYPES
# =========================

# Numeric columns
df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
df["price_per_unit"] = pd.to_numeric(df["price_per_unit"], errors="coerce")
df["total_spent"] = pd.to_numeric(df["total_spent"], errors="coerce")

# Date column
df["transaction_date"] = pd.to_datetime(df["transaction_date"], errors="coerce")

# =========================
# 5. REBUILD TOTAL_SPENT (DATA FIX)
# =========================
df["total_spent"] = df["quantity"] * df["price_per_unit"]

# =========================
# 6. CLEAN TEXT COLUMNS
# =========================
text_cols = ["item", "payment_method", "location"]

for col in text_cols:
    df[col] = df[col].astype(str).str.strip().str.title()
    df[col] = df[col].replace("Nan", np.nan)

# =========================
# 7. HANDLE MISSING VALUES
# =========================

# Categorical columns
df["item"] = df["item"].fillna("Unknown Item")
df["payment_method"] = df["payment_method"].fillna("Unknown Payment")
df["location"] = df["location"].fillna("Unknown Location")

# Drop rows where critical numeric data is missing
df = df.dropna(subset=["quantity", "price_per_unit", "total_spent"])

# =========================
# 8. REMOVE DUPLICATES
# =========================
df = df.drop_duplicates(subset=["transaction_id"])

# =========================
# 9. OUTLIER REMOVAL (IQR METHOD)
# =========================
Q1 = df["total_spent"].quantile(0.25)
Q3 = df["total_spent"].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df = df[(df["total_spent"] >= lower_bound) & (df["total_spent"] <= upper_bound)]

# =========================
# 10. FINAL QUALITY CHECK
# =========================
print(df.info())
print(df.isnull().sum())
print(df.describe())

# =========================
# 11. EXPORT CLEAN DATA
# =========================
df.to_csv("clean_cafe_sales.csv", index=False)