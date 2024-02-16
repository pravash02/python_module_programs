import pandas as pd
import numpy as np


data = {
    'C': [5, 2, 8],
    'B': [0, 3, 1],
    'A': [10, 6, 7]
}
df = pd.DataFrame(data)
print(df)

# Sort the columns
sorted_columns = df.columns.sort_values()
print(sorted_columns)

# Sort the DataFrame based on the sorted columns
sorted_df = df[sorted_columns].sort_values(by=list(sorted_columns), axis=0).reset_index(drop=True)
print(sorted_df)


sorted_df2 = df[sorted_columns].apply(lambda x: x.sort_values().values)
print(sorted_df2)


print(df[sorted_columns].transform(np.sort))



