import pandas as pd

df = pd.read_csv("C:/Users/surya/Downloads/car_sales.csv")

date = pd.DatetimeIndex(df['date'])
df['month']=date.month

sales = df.groupby(['Manufacturer','month']).sum('Sales_in_thousands').sort_values(['month','Sales_in_thousands'],ascending=False)
top=df.groupby('month').head(5)

print(top)