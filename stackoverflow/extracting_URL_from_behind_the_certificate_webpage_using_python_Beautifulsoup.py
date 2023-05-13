import requests
from bs4 import BeautifulSoup


# Example
html_data = """
<html>
<head>
    <title>Sample Page</title>
</head>
<body>
    <h1>Welcome to the Sample Page</h1>
    <p>This is a paragraph.</p>
    <a href="https://www.example.com">Link 1</a>
    <a href="https://www.google.com">Link 2</a>
    <a href="https://www.github.com">Link 3</a>
</body>
</html>
"""

soup = BeautifulSoup(html_data, "html.parser")

link_tags = soup.find_all("a", href=True)

for link in link_tags:
    url = link.get("href")
    print(url)


## Solution
# with open(fr"B:\allCerts\cert.pem", 'rb') as file:
#     pem_data = file.read()
#
# response = connection.get(url, cert=pem_data)
#
# if response.status_code == 200:
#     XMLurls = BeautifulSoup(response.content, "html.parser")
#
#     href_urls = XMLurls.find_all("a", href=True)[::2]
#     for link in XMLurls:
#         url = link.get("href")
#         print(url)
