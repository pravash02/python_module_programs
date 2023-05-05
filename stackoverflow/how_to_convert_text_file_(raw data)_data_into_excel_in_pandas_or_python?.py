import pandas as pd

# data = pd.read_csv('text_file.txt', delimiter='-', skiprows=1, engine='python', names=['Host address', 'Host address (decimal)', 'Host address (hex)', 'Net address', 'Networker', 'Remaining'])

# for i in range(0, len(data), 6):
#     host_address = data['Value'][i]
#     host_address_decimal = data['Value'][i+1]
#     host_address_hex = data['Value'][i+2]
#     net_address = data['Value'][i+3]
#     networker = data['Value'][i+4]
#
#     new_row = {'Host address': host_address, 'Host address (decimal)': host_address_decimal, 'Host address (hex)': host_address_hex, 'Net address': net_address, 'Networker': networker, '/remaining': ''}
#     new_data = new_data.append(new_row, ignore_index=True)
#
# print(new_data['Host address', 'Host address (decimal)', 'Host address (hex)'])


with open('text_file.txt', 'r') as f:
    text_file_data = f.read()

rows = text_file_data.strip().split('\n\n')

list_data = []
for record in rows:
    lines = record.split('\n')
    # print(lines)

    record_dict = {}
    for line in lines:
        if '-' in line and 'ipv' not in line:
            key, value = line.split('-', 1)
            record_dict[key.strip()] = value.strip()
    list_data.append(record_dict)
print(list_data)

df = pd.DataFrame(list_data)
df = df[['Host address', 'Host address (decimal)', 'Host address (hex)', 'Net address', 'Networker']]

# df.columns = ['Host address', 'Host address (decimal)', 'Host address (hex)', 'Net address', 'Networker /remaining']
# df['Networker /remaining'] = df['Networker'] + df['Networker /remaining'].fillna('')
# df.drop('Networker', axis=1, inplace=True)

print(df)
