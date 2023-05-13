from io import StringIO
import requests
import pandas as pd


repo_owner = 'pravash02'
repo_name = 'python_module_programs'
file_path = 'stackoverflow/df_pf.csv'

url = f'https://github.com/{repo_owner}/{repo_name}/blob/main/{file_path}'
print(url)

response = requests.get(url)
# print(response.text)

df = pd.read_csv(StringIO(response.text))

csv_data = df.to_csv(index=False)

headers = {
    'Authorization': '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',
    'Content-Type': 'application/octet-stream',
}

update_url = f'https://github.com/{repo_owner}/{repo_name}/blob/main/{file_path}'
print(update_url)

data = {
    'message': 'Update CSV file',
    'content': csv_data
}

response = requests.put(update_url, headers=headers, json=data)
