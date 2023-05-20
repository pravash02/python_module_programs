import pandas as pd

# LIST OF DICT to dataframe
data = [
    {
        'Area of expertise': ['Acne', 'Skin cancer', 'Moles'],
        'Health insurance': ["I'm paying for myself", 'Alliance Health Group', 'Allianz', 'AVIVA'],
        'Language spoken': ['English', 'Hindi'],
        'Name': 'Nikhil',
        'Ratings': '5',
        'Types of offering': ['Call']
    },
    {
        'Area of expertise': ['Acne', 'Skin cancer', 'Moles', 'Lichen sclerosus', 'Psoriasis'],
        'Health insurance': ["I'm paying for myself"],
        'Language spoken': ['English'],
        'Name': 'Akhil',
        'Ratings': '5',
        'Types of offering': ['Call']
    }
]

df = pd.DataFrame(data)
# df.to_excel('dict_data.xlsx', engine='openpyxl', index=False)
# df.to_csv('dict_data.csv', index=False)


# CONCAT new data in dataframe list column
order_info = {
    "order id": 1,
    "order status": "Placed",
    "order time": 1683903935860,
    "table": 212,
    "order items": ["leek", "chicken"]
}
order_info_df = pd.DataFrame([order_info])
new_item = ["steak", "beef"]

order_info_df.loc[order_info_df['order id'] == 1, 'order items'] = order_info_df.loc[order_info_df['order id'] == 1, 'order items'].apply(lambda x: x + new_item)
# print(order_info_df)


# MERGE
df_1 = pd.DataFrame({'id': [123], 'name': ['Pupkin Vasya'], 'email': ['Pupkin_Vasya@mail.ru'], 'usless_info': [1]})
df_2 = pd.DataFrame({'id': [123], 'phone': [79999999999], 'usless_info': [1]})
df = pd.merge(left=df_2[['id', 'phone']], right=df_1[['id', 'name', 'email']], how='left', on='id')
print(df)
# df.to_csv('final.csv', index=False)


# DELETE all lines before 2000th line index
# df = df.drop(df[df.index < 2000].index)




