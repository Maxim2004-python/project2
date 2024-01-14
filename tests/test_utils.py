from config import TEST
from src.utils import open_, executed_satatus


def test_open_():
    assert open_(TEST) == [1, 2, 3]

def test_executed_satatus():
    assert executed_satatus([{'state': 'EXECUTED'},
                             {'state': 'WORD'},
                             {}]) == [{'state': 'EXECUTED'}]

