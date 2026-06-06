import pandas as pd

df = pd.read_csv('dirty_cafe_sales.csv')

# Basic info
#print(df.shape)
#print(df.dtypes)
#print(df.head())
#print(df.isnull().sum())

# Clean: drop rows with UNKNOWN/ERROR in key columns
        #If there are unknonwn, error in their rows, entire row gets deleted
df = df[~df['Item'].isin(['UNKNOWN', 'ERROR'])]
df = df[~df['Payment Method'].isin(['UNKNOWN', 'ERROR'])]
df = df[~df['Location'].isin(['UNKNOWN', 'ERROR'])]
df = df[~df['Total Spent'].isin(['UNKNOWN', 'ERROR'])]
df = df.dropna(subset=['Item', 'Payment Method', 'Location', 'Total Spent'])

# Cast types
df['Quantity']         = pd.to_numeric(df['Quantity'],       errors='coerce')
df['Price Per Unit']   = pd.to_numeric(df['Price Per Unit'], errors='coerce')
df['Total Spent']      = pd.to_numeric(df['Total Spent'],    errors='coerce')
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'], errors='coerce')

# Stats
print(df.shape)
print(df['Total Spent'].describe())
print(df['Item'].value_counts())
print(df['Payment Method'].value_counts())
print(df['Location'].value_counts())
print(df.groupby('Item')['Total Spent'].sum().sort_values(ascending=False))
print(df.groupby('Payment Method')['Total Spent'].sum().sort_values(ascending=False))
print(df.groupby('Location')['Total Spent'].sum().sort_values(ascending=False))

# Export
df.to_csv("cleand.csv", index=False)