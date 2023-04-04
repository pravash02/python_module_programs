import bonobo
import json


def extract():
    with open('./data/data.csv') as f:
        for line in f:
            yield line.strip().split(',')


def transform(*row):
    return {
        'name': row[0][0],
        'age': row[0][1],
        'city': row[0][2]
    }


def load(data):
    with open('data.json', 'w') as f:
        f.write(json.dumps(data, indent=2))


graph = bonobo.Graph(
    extract,
    transform,
    load,
)

if __name__ == '__main__':
    bonobo.run(graph)
