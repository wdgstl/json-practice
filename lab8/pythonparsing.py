import json

with open('/home/wdgstl/DS2002/json-practice/data/schacon.repos.json', 'r') as file:
    data = json.load(file)
    csv_lines = []
    for r in data:
        csv_line = ''
        csv_line += str(r["name"])
        csv_line += ',' + str(r["html_url"])
        csv_line += ',' + str(r["updated_at"])
        csv_line += ',' + str(r["visibility"])
        csv_lines.append(csv_line)

with open('/home/wdgstl/DS2002/json-practice/data/chacon.csv', 'w',encoding='UTF8') as file:
    for line in csv_lines[:5]:
        file.write(f'{line}\n')

