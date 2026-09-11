import pandas as pd

# Load cleaned retail sales data
df = pd.read_csv('data/retail_sales_clean.csv')

print('Dataset shape:', df.shape)
print('\nData types:\n', df.dtypes)
print('\nDescriptive statistics:\n', df.describe())
print('\nSales by category:\n', df.groupby('Category')['Sales'].sum().sort_values(ascending=False))
print('\nSales by region:\n', df.groupby('Region')['Sales'].sum().sort_values(ascending=False))
print('\nTop products:\n', df.groupby('Product')['Sales'].sum().sort_values(ascending=False).head(10))
