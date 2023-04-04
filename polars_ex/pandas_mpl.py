import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./polars_ex/stock_prices.csv')
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
plt.plot(df['Close'])
plt.title('Closing Prices')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
