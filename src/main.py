from src.utils import change_numbers, sorted_data, time_corrected


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

main(sorted_data)

