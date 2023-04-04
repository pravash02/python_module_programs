import pandasql
from pandasql import sqldf
import pandas as pd
import sqlite3

# create two sample dataframes
df1 = pd.DataFrame({'col1': [1, 2, 3, 4, 5], 'col2': ['a', 'b', 'c', 'd', 'e']})
df2 = pd.DataFrame({'col2': ['a', 'b', 'c', 'f'], 'col3': [10, 20, 30, 40]})

# conn = sqlite3.connect('my_database.db')
# schema = pd.io.sql.SQLDatabase(conn)

# define the SQL query
query = """SELECT * FROM df1 INNER JOIN df2 ON df1.col2 = df2.col2 WHERE df1.col1 > 2;"""

# run the SQL query on the dataframes using pandasql
# pysqldf = lambda q: sqldf(q, locals())
# result = pysqldf(query)
result = sqldf(query, locals())
print(result)
