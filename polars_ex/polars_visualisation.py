import polars as pl
import matplotlib.pyplot as plt

# Create a DataFrame with some data
data = {'fruit': ['apple', 'banana', 'orange', 'apple', 'banana', 'orange'],
        'year': [2019, 2019, 2019, 2020, 2020, 2020],
        'sales': [100, 200, 150, 120, 250, 180]}
df = pl.DataFrame(data)

# Group the data by fruit and year, and calculate the sum of sales
grouped_df = df.groupby('year', maintain_order=True).sum()
print(grouped_df)

# pandas_df = grouped_df.to_pandas().unstack()
# pandas_df.plot.bar(rot=0)

# Convert the resulting DataFrame to a pandas DataFrame for plotting
grouped_df.to_pandas().unstack().plot(kind='bar', stacked=True)

# Show the plot
plt.show()
