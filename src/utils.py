import json

from config import DATA, TEST

from datetime import datetime


def open_(data):
    with open(data, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def executed_satatus(data):
    executed_operations = []
    for operation in data:
        if operation.get('state') == 'EXECUTED':
            executed_operations.append(operation)
    return executed_operations




def date_sorted(data):
    return sorted(data, key=lambda dictionary: dictionary['date'], reverse=True)[:5]


data_load = open_(DATA)

executed_data = executed_satatus(data_load)

sorted_data = date_sorted(executed_data)

print(len(sorted_data))

