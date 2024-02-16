import asyncio

import pandas as pd
import csv

f = 'test.dat'


with open(f, 'r') as file:
    dialect = csv.Sniffer().sniff(file.read(1024))
    delimiter = dialect.delimiter

print(delimiter)
df = pd.read_csv(f, sep=delimiter, engine='python')
# print(df)


df1 = pd.read_csv(f, header=0, engine='python')
print(df1.columns[0])
delimiter = df1.columns[0][-1]
print('delimiter - ', delimiter)



