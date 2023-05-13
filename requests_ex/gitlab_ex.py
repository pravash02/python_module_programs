from io import StringIO
import requests
import pandas as pd


repo_owner = ''
repo_name = ''
file_path = 'stackoverflow/client.csv'

url = f'https://github.com/{repo_owner}/{repo_name}/blob/main/{file_path}'
print(url)

response = requests.get(url)
# print(response.text)

df = pd.read_csv(StringIO(response.text))

csv_data = df.to_csv(index=False)

headers = {
    'Authorization': '',
    'Content-Type': 'application/octet-stream',
}

update_url = f'https://github.com/{repo_owner}/{repo_name}/blob/main/{file_path}'
print(update_url)

data = {
    'message': 'Update CSV file',
    'content': csv_data
}

response = requests.put(update_url, headers=headers, json=data)
