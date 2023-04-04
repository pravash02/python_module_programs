import polars as pl
import pandas as pd
import time


df = pl.read_csv('stock_prices.csv')
df_filtered = df.filter(pl.col("Volume") > 49321000)
df_grouped = df_filtered.groupby("Date").agg({"Volume": "mean"})


start_time = time.time()
# read CSV file into Polars data frame
df = pl.read_csv('stock_prices.csv')
# calculate daily percentage change in close price
df = df.with_columns(pl.col('Close').pct_change().alias('daily_pct_change'))
# identify top 10 days with largest percentage change
df_top10 = df.sort("daily_pct_change", descending=True).limit(10)
end_time = time.time()
print("Polars Execution time {:0.2f}s".format(end_time-start_time))


df = pl.read_csv('stock_prices.csv')
filtered_df = df.filter(pl.col('Volume') == 54937200)
# print(filtered_df)


start_time = time.time()
# read CSV file into Pandas data frame
df = pd.read_csv("stock_prices.csv")
# calculate daily percentage change in close price
df["daily_pct_change"] = (df["Close"] / df["Close"].shift(1)) * 100
# identify top 10 days with largest percentage change
df_top10 = df.nlargest(10, "daily_pct_change")
end_time = time.time()
print("Pandas Execution time {:0.2f}s".format(end_time-start_time))
