from config import TEST
from src.utils import open_


def test_open_():
    assert open_(TEST) == [1, 2, 3]
