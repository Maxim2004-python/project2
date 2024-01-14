import json

from config import DATA, TEST

from datetime import datetime


def open_(data):
    with open(data, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


# def executed_satatus(data):
#     for operation in data:
#         if operation['state'] == 'EXECUTED':
#             return operation
#
#
#
# def date_sorted(data):
#     for object in data:
#         datetime_object = datetime.strptime(object['date'], '%Y-%m-%dT%H:%M:%S.%f')
#         new_date_str = datetime_object.strftime('%d.%m.%Y')
#         object['date'] = new_date_str
#     return data



