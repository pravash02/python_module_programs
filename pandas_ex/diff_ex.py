import pandas as pd
from dateutil.parser import parse

df1 = pd.DataFrame({'1': [30, 20, 40], '2': [30, 20, 40], '3': [30, 20, 40], '4': [30, 20, 40]}, index=['A', 'B', 'C'])
df2 = pd.DataFrame({'1': [30, 20, 40], '2': [30, 20, 40], '3': [30, 20, 40], '4': [30, 20, 10]}, index=['A', 'B', 'C'])

# df_diff = df1.sub(df2, fill_value=0)
# print(df_diff)
# df = df_diff.add(df2, fill_value=0)
# print(df)

# print(df1.equals(df2))

miss_matched_col = []
for column in df1.columns:
    if column in df2.columns:
        if not df1[column].equals(df2[column]):
            miss_matched_col.append(column)
# print(miss_matched_col)

# cmp_df = df1.compare(df2, keep_equal=False)
# print(cmp_df)


# Sample DataFrame with date column having different formats
data = {
    'date_column': ['2023-08-02', '08/02/2023', '2023-02-08', '02/08/2023', '2023-03-15', '15-Mar-2023'],
    'other_column': [10, 20, 30, 40, 50, 60]
}
df = pd.DataFrame(data)


# Function to parse date strings with dateutil.parser.parse()
def parse_date(date_str):
    try:
        return parse(date_str)
    except ValueError:
        return None


# Apply the parse_date function to the date_column
df['parsed_date'] = df['date_column'].apply(parse_date)
# print(df)

column_info = {'col1': 'VARCHAR2'}
oracle_to_pandas_dtype = {
    'VARCHAR2': 'object',
    'NUMBER': 'float64',
}

# Convert the results into a dictionary with mapped data types
meta = {column: oracle_to_pandas_dtype.get(dtype, dtype) for column, dtype in column_info.items()}
# print(meta)


# Create sample DataFrames
data1 = {'A': [0, 0, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
data2 = {'A': [1, 2, 4], 'B': [4, 5, 7], 'C': [7, 8, 9]}

df1 = pd.DataFrame(data1, index=['row1', 'row2', 'row3'])
df2 = pd.DataFrame(data2, index=['row1', 'row2', 'row3'])

# List of columns to compare
columns_to_compare = ['A', 'B']

# Initialize an empty DataFrame to store comparison results
comparison_result = pd.DataFrame()
comp_result = pd.DataFrame()

# Compare specified columns and append results to the new DataFrame
# for col in columns_to_compare:
#     comp_result = df1[col].compare(df2[col], align_axis=1)
#     print(comp_result)
#     comparison_result = comparison_result._append(comp_result)

cmp_res = pd.DataFrame()
for col in columns_to_compare:
    comp_result = df1[col].compare(df2[col], keep_equal=False)
    # comp_result.columns = pd.MultiIndex.from_tuples([(col, 'src'), (col, 'cmp'), ()])
    comp_result.columns = pd.MultiIndex.from_product([[col], ['src', 'cmp']])
    comp_result.insert(0, ('', 'Row'), comp_result.index)
    comparison_result = pd.concat([comparison_result, comp_result], axis=1)
    # for index, data in comp_result.iterrows():
        # row_data = {('Column', 'src'): [col, data['self']], ('Column', 'cmp'): [col, data['other']], ('Row', ''): [index, '']}
        # comparison_result = comparison_result._append(row_data, ignore_index=True)

    # cmp_res = pd.concat([cmp_res, comp_result])

# print(cmp_res)
print(comparison_result.reset_index(drop=True))

