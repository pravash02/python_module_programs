import pandas as pd
import numpy as np

s = pd.Series([1, 2, 3, 0, 4, 0, 5, 6, 0])
mask = s == 0

s.loc[mask] = np.random.randint(100, 1000, size=mask.sum())
# print(s)


df = pd.DataFrame({
    'A': [1, 0, 3, 0, 5],
    'B': [0, 2, 0, 4, 0],
    'C': [6, 7, 0, 9, 10]
})

mask = df == 0

cols = [list(mask.columns)]
df.iloc[mask] = np.random.randint(100, 1000, size=mask.sum().sum())

print(df)
