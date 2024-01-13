import json


def open_():
    with open ('operations.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    return data

print(open_())
