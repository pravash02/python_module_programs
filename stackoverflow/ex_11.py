# import fileinput
#
#
# def delete_line(file_path, line_number):
#     with fileinput.FileInput(file_path, inplace=True, backup='.bak') as file:
#         for line_index, line in enumerate(file, 1):
#             if line_index != line_number:
#                 print(line, end='')
#
#
# delete_line('del_fil.txt', 4)
#
#

import pandas as pd

d = {'col1': ["ABC1"+"\n"+"ABC2"+"\n"+"ABC3", "BBC1"+"\n"+"BBC2"+"\n"+"BBC3"], 'col2': ["A"+"\n"+"B"+"\n"+"C", "A"+"\n"+"B"+"\n"+"C"],'col3': ["YES"+"\n"+"NO"+"\n"+"YES", "NO"+"\n"+"NO"+"\n"+"YES"]}
df = pd.DataFrame(data=d)
print(df)

# cols=['col1','col2','col3']

# df['DesiredCol'] = df[cols].apply(lambda row: ' '.join(row.values.astype(str)), axis=1)
# print(df)


def concatenate_row(row):
    return " ".join(row.split("\n"))

# df["DesiredCol"] = df.apply(lambda row: concatenate_row(row["col1"]) + " " + concatenate_row(row["col2"]) + " " + concatenate_row(row["col3"]), axis=1)

df["DesiredCol"] = df.apply(lambda row: "\n".join(value for col in zip(row["col1"].split("\n"), row["col2"].split("\n"), row["col3"].split("\n")) for value in col), axis=1)

# Drop the original columns if needed
df.drop(columns=["col1", "col2", "col3"], inplace=True)
print(df)
