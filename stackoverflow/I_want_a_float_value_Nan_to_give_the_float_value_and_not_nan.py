import pandas as pd

df1 = pd.DataFrame({'1': [30, 20, 40], '2': [30, 20, 40], '3': [30, 20, 40], '4': [30, 20, 40]}, index=['A', 'B', 'C'])
df2 = pd.DataFrame({'1': [10, 5, 0], '2': [10, 5, 0], '3': [30, 5, 0], '4': [10, 5, 0]}, index=['A', 'B', 'D'])

df_diff = df1.sub(df2, fill_value=0)
print(df_diff)
# df = df_diff.add(df2, fill_value=0)
# print(df)
