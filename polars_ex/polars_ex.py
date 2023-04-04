import pandas as pd
import polars as pl
import matplotlib.pyplot as plt

df = pl.read_csv('stock_prices.csv')
print(df)
plt.plot(df['Close'])
plt.title('Closing Prices')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
# plt.plot(df, x='Date', y='Close', width=800, height=400, title='Closing Prices', interactive=True)
