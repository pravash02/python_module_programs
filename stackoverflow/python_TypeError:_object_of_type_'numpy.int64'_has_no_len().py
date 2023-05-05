import pandas as pd


data = {'ID': ['1', '2', '2', '3'],
        'Name': ['Jack', 'John', 'Steve', 'James']}

df = pd.DataFrame(data)

with pd.ExcelWriter('output.xlsx', engine='openpyxl', mode='w') as writer:
    for name in df['ID'].unique():
        temp_df = df[df['ID'] == name]
        print(temp_df)
        temp_df.to_excel(writer, sheet_name=str(name))

