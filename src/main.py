from config import DATA
from src.utils import change_numbers, sorted_data, time_corrected, open_, executed_satatus, date_sorted


def main(sorted_data):
    time_corrected(sorted_data)
    for i in sorted_data:
        if i.get('from') is None:
            print(f"{i['date']} {i['description']}\n"
                  f"Операция со счётом -> {change_numbers(i['to'])}\n"
                  f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}\n")
        else:
            print(f"{i['date']} {i['description']}\n"
                  f"{change_numbers((i.get('from')))} -> {change_numbers(i['to'])}\n"
                  f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}\n")

data_load = open_(DATA)

executed_data = executed_satatus(data_load)

sorted_data = date_sorted(executed_data)

main(sorted_data)

