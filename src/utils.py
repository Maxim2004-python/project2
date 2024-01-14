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
    new_list = []
    for time in data:
        wrong_time = date.strptime(time['date'], '%Y-%m-%dT%H:%M:%S.%f')
        time['date'] = wrong_time.strftime('%d.%m.%Y')
        new_list.append(time)
    return(new_list)


def change_numbers(key_card_info):
    new_list = []
    split_card_info = key_card_info.split()
    for item in split_card_info:
        if 'Счет' in key_card_info and item.isdigit():
            new_list.append(f'{item[-4:]}')
        elif 'Счет' not in key_card_info  and item.isdigit():
            new_list.append(f'{item[:4]} {item[4:6]} **** {item[-4:]}')
        else:
            new_list.append(item)
    return ' '.join(new_list)










data_load = open_(DATA)

executed_data = executed_satatus(data_load)

sorted_data = date_sorted(executed_data)

changed_data = time_corrected(sorted_data)

new_numebrs = change_numbers(changed_data)

print(sorted_data)

