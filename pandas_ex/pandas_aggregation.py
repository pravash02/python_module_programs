import pandas as pd
import sqlalchemy

data1 = {'id': [1, 2, 3, 1, 2, 3],
         'fruit': ['apple', 'banana', 'orange', 'apple', 'banana', 'orange'],
         'year': [2019, 2019, 2019, 2020, 2020, 2020],
         'sales': [100, 200, 150, 120, 250, 180]}
table_1 = pd.DataFrame(data1)

data2 = {'id': [1, 2, 3, 1, 2, 3],
         'season': ['winter', 'summer', 'summer', 'spring', 'monsoon', 'winter']}
table_2 = pd.DataFrame(data1)

# table_1 = pd.read_sql_table('table_1', engine)
# table_2 = pd.read_sql_table('table_2', engine)

# Perform a left join between the two dataframes on col2
merged = pd.merge(table_1, table_2, on='id', how='left')
print(merged)

# # Filter the resulting dataframe for rows where col5 is equal to the maximum value of col5 where col4 is 'some_value' in table_2
# max_col5 = table_2[table_2['col4'] == 'some_value']['col5'].max()
# filtered = merged[merged['col5'] == max_col5]
#
# # Add col1, col2, and col3 to the resulting dataframe
# filtered['col1'] = table_2['col1']
# filtered['col2'] = table_2['col2']
# filtered['col3'] = table_2['col3']

# Insert the resulting dataframe into table_1
# filtered.to_sql('table_1', engine, if_exists='append', index=False)