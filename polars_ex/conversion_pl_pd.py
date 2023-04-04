import polars as pl
import pandas as pd

# create a Pandas data frame
df_pandas = pd.DataFrame({
'A': [1, 2, 3],
'B': [4, 5, 6],
'C': [7, 8, 9]
})
# convert to Polars data frame
df_polars = pl.from_pandas(df_pandas)


# create a Polars data frame
df_polars = pl.DataFrame({
'A': [1, 2, 3],
'B': [4, 5, 6],
'C': [7, 8, 9]
})
# convert to Pandas data frame
df_pandas = df_polars.to_pandas()
