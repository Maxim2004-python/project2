from src.utils import change_numbers, sorted_data


def main(sorted_data):
    for i in sorted_data:
        print(f"""{i['date']} {i['description']} 
{change_numbers(i['from'])} -> {change_numbers(i['to'])}
{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}""")

main(sorted_data)

