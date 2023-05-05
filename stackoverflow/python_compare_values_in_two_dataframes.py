import pandas as pd

# Create two example dataframes
df1 = pd.DataFrame({'locid': [1, 2, 3], 'locname': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'locid': [1, 3, 4], 'locname': ['Anna', 'Tim', 'Dave']})

# Inner join the two dataframes on the 'id' column
result = pd.merge(df1, df2, on='locid', suffixes=['_table1', '_table2'])

# Display the result dataframe
print(result)
