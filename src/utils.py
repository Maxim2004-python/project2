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


data_print = open_(DATA)

print(executed_satatus(data_print))

#
#
#
# def date_sorted(data):
#     for object in data:
#         datetime_object = datetime.strptime(object['date'], '%Y-%m-%dT%H:%M:%S.%f')
#         new_date_str = datetime_object.strftime('%d.%m.%Y')
#         object['date'] = new_date_str
#     return data



