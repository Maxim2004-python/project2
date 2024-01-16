from config import TEST
from src.utils import open_, executed_satatus, date_sorted, time_corrected, change_numbers


def test_open_():
    assert open_(TEST) == [1, 2, 3]

def test_executed_satatus():
    assert executed_satatus([{'state': 'EXECUTED'},
                             {'state': 'WORD'},
                             {}]) == [{'state': 'EXECUTED'}]

def test_date_sorted():
    assert date_sorted([{'date': '2019-08-26T10:50:58.294041'},
                             {'date': '2019-06-14T19:37:49.044089'},
                             {'date': '2019-10-30T01:49:52.939296'}]) == [{'date': '2019-10-30T01:49:52.939296'},
                                                                          {'date': '2019-08-26T10:50:58.294041'},
                                                                          {'date': '2019-06-14T19:37:49.044089'}
                                                                          ]

def test_time_corrected():
    func = [{'date': '2019-08-26T10:50:58.294041'},
                             {'date': '2019-06-14T19:37:49.044089'},
                             {'date': '2019-10-30T01:49:52.939296'}]
    time_corrected(func)
    assert func == [{'date': '26.08.2019'},
                             {'date': '14.06.2019'},
                             {'date': '30.10.2019'}]

def test_change_numbers():
    assert change_numbers("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    assert change_numbers("Счет 64686473678894779589") == "Счет **9589"

