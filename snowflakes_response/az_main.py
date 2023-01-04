from urllib.parse import urlparse, parse_qs
import json
import azure.functions as func


def main(req: func.HttpRequest) -> str:
    param = ''
    op = urlparse(req)
    query = parse_qs(op.query)
    servicename = query.get('param')
    print('servicename -', servicename)
    with open('mapping.json', 'r') as data:
        data = json.load(data)
    if servicename in list(data.keys()):
        param = data[servicename]
        print(param)
    print(param)
    return param


if __name__ == '__main__':
    main(req='http://localhost:7071/api/endpoint?param=AAD')
