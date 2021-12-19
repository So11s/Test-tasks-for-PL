import json

with open('../tests.json', 'r') as file:
    data = json.load(file)

with open('../values.json', 'r') as file_2:
    todos = json.load(file_2)

for k, v in todos.items():

        for i in v:

            for t, y in data.items():

                if i.get('id') == data.get('id'):
                    data['value'] = i['value']

                elif isinstance(y,list):

                    for elem in y:

                        if i.get('id') == elem.get('id'):
                            elem['value'] = i['value']

with open('../report.json', 'w', encoding='utf8') as rep:
    json.dump(data, rep, indent=4)