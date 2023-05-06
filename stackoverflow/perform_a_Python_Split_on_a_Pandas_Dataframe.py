import pandas as pd

data = {
    'Test_Step_ID': ['9.1.1', '9.1.2', '9.1.3', '9.1.4'],
    'Protocol_Name': ['A', 'B', 'C', 'D'],
    'Req_ID': ['SRS_0081d', 'SRS_0079', 'SRS_0082SRS_0082a', 'SRS_0015SRS_0015cSRS_0015d']
}
df = pd.DataFrame(data)

df['Req_ID'] = df['Req_ID'].str.split('SRS_')
df = df.explode('Req_ID')

df['Req_ID'] = df['Req_ID'].str.strip()
df = df[df['Req_ID'].ne('')]

df['Req_ID'] = 'SRS_' + df['Req_ID']
print(df)

# out = (df
#        .assign(Req_ID=df['Req_ID'].str.split(r'(?<=.)(?=SRS)'))
#        .explode('Req_ID')
#        )
# print(out)
