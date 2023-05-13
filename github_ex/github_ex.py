import subprocess
from io import StringIO
import requests
import pandas as pd
import git
from github import Github


repo_owner = 'pravash02'
repo_name = 'python_module_programs'
file_path = 'stackoverflow/client.csv'
token = ''
commit_message = 'Update CSV file'

github = Github(token)
repo = github.get_user(repo_owner).get_repo(repo_name)

url = f'https://raw.githubusercontent.com/{repo_owner}/{repo_name}/main/{file_path}'
response = requests.get(url)
df = pd.read_csv(StringIO(response.text))

df['test'] = "new_test_val"

content = repo.get_contents(file_path)

df.to_csv("../" + file_path, index=False)

with open("../" + file_path, 'rb') as file:
    contents = file.read()

repo.update_file(file_path, commit_message, contents, content.sha)
