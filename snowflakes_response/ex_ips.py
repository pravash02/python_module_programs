import json
import requests
from bs4 import BeautifulSoup
import sys

# global variable
param = ''


def main():
    res_ips = {}
    status_code = 500

    try:
        # request page
        URL = "https://www.microsoft.com/en-us/download/confirmation.aspx?id=56519"
        page = requests.get(URL)

        ip_param = sys.argv[1]
        with open('snowflakes_response/mapping.json', 'r') as data:
            data = json.load(data)
        if ip_param in data.keys():
            param = data[ip_param]

        # parse HTML to get the real link
        soup = BeautifulSoup(page.content, "html.parser")
        link = soup.find('a', {'data-bi-containername': 'download retry'})['href']

        ### download
        file_download = requests.get(link)
        print(type(file_download.content.decode('utf-8')))

        ### save in azure_ips.json
        # open("azure_ips.json", "wb").write(file_download.content)
        # Reading json file
        # with open('azure_ips.json', 'r') as JSON:
        #    json_dict = json.load(JSON)

        json_dict = json.loads(file_download.content.decode('utf-8'))
        list_ips = []
        for i in range(len(json_dict['values'])):
            if json_dict['values'][i]['name'] == param:
                list_ips.append([0, json_dict['values'][i]['properties']['addressPrefixes']])

        res_ips['data'] = list_ips
        status_code = 200

    except Exception as e:
        status_code = 400
        # print(e)
        res_ips['data'] = [[0, '']]

    response = {
        "statusCode": status_code,
        "headers": {"Content-Type": "application/json"},
        "body": res_ips
    }
    print(response)


if __name__ == '__main__':
    try:
        # ip_param = sys.argv[1]
        # with open('snowflakes_response/mapping.json', 'r') as data:
        #     data = json.load(data)
        # if ip_param in data.keys():
        #     param = data[ip_param]
        main()
        # else:
        #     raise ValueError("parameter not found in mapping file")
    except Exception as e:
        print(e)
