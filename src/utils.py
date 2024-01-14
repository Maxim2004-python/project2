import json

from config import DATA, TEST

from datetime import datetime as date


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

def time_corrected(data):
    for time in data:
        wrong_time = date.strptime(time['date'], '%Y-%m-%dT%H:%M:%S.%f')
        time['date'] = wrong_time.strftime('%d.%m.%y')


data_load = open_(DATA)

executed_data = executed_satatus(data_load)

sorted_data = date_sorted(executed_data)

changed_data = time_corrected(sorted_data)

print(sorted_data)

