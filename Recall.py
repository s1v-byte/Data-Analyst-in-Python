import pandas as pd

# IMPORTING THE FILE
df = pd.read_csv("dirty_cafe_sales.csv")
#df1 = pd.read_excel("dity_cafe_sales.excel")

# INSPECT THE DATA
#print(df.head())
#df.info() #Found out that 
#print(df.describe()) #Tells how many are unique and repeated per column #top = mode #freq count of most common value
#print(df.shape)#See how many rows, columns

# CREATING BACKUP
df_raw = df.copy()

# rEMOVING DUPLICATES
df = df.drop_duplicates() #As a whole 
df = df.drop_duplicates(subset = ["Transaction ID"]) #<-- Removes duplicates from Transaction ID

# REPLACING SPACES FROM COLUMNS INTO _
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# IDENTIFY MISSING VALUES
#print(df.isnull().sum()) 
#print(df.isnull().sum() / len(df) * 100) #In Percentage format



# Convert numeric columns
for col in ["quantity", "price_per_unit", "total_spent"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# UPPERCASING ALL THE ROWS FROM SPECIFIC COLUMN
df["item"] = df["item"].str.upper()

# Remove rows with missing values
df = df.dropna()

#print(df.describe())
print(df.head())
print(df.groupby("item")["quantity"].mean())
