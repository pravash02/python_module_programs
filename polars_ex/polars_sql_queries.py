import polars as pl

data = {'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35],
        'salary': [50000, 60000, 70000]}

df = pl.DataFrame(data)
print(df.dtypes)

query = """select name, age, salary from df where age > 25;"""

result = df.lazy().filter(query)
result.collect()
