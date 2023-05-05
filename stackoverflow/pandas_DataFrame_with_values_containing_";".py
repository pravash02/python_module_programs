import csv
import pandas as pd

dataframe = pd.read_csv(
    f'df_pf.csv',
    engine='python',
    encoding='cp1252',
    sep=';',
    quotechar='"',
    escapechar='\\',
    quoting=csv.QUOTE_NONE,
    header=None
)

for col in dataframe.columns:
    dataframe[col] = dataframe[col].str.replace('"', '')

print(dataframe)
