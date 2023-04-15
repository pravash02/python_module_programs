import pandas as pd


df1 = pd.DataFrame(data={'col1': [1, 2, 3, 4, 5, 3],
                         'col2': [10, 11, 12, 13, 14, 10]})
df2 = pd.DataFrame(data={'col1': [1, 2, 3],
                         'col2': [10, 11, 12]})
df3 = pd.DataFrame(data={'col1': [2, 3, 4],
                         'col2': [11, 12, 13]})

new_df1 = df1.loc[~df1.set_index(list(df1.columns)).index.isin(df3.set_index(list(df3.columns)).index)]
print(new_df1)


data1 = pd.read_csv("sample_1.csv")
data2 = pd.read_csv("sample_2.csv")

new_df2 = data2.loc[~data2.set_index(list(data2.columns)).index.isin(data1.set_index(list(data1.columns)).index)]
print(new_df2)

