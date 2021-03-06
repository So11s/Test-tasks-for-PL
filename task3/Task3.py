import json
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("tests")
parser.add_argument("values")

args = parser.parse_args()

with open(args.tests, 'r', encoding='utf-8') as file:
    data = json.load(file)

with open(args.values, 'r', encoding='utf-8') as file_2:
    todos = json.load(file_2)


def task3(sqr, sqr2):
    if isinstance(sqr, dict):
        for k, v in sqr.copy().items():
            if isinstance(v, list):
                for i in v:
                    if isinstance(i, dict):
                        task3(i, sqr2)
            else:
                for t, y in sqr2.items():
                    for elem in y:
                        if sqr['id'] == elem['id'] and sqr.get('value') == '':
                            sqr['value'] = elem['value']

    with open('report.json', 'w', encoding='utf-8') as rep:
        json.dump(data, rep, indent=4)

task3(data, todos)