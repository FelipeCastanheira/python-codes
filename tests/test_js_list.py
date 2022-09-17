from classes.js_list import js_list
import pytest


@pytest.fixture
def names():
    """Nosso cenário (word) temos a seguinte palavra"""
    return js_list(["Celia", "Queipe", "Lelso", "Fezio"])


@pytest.fixture
def numbers():
    """Nosso cenário (word) temos a seguinte palavra"""
    return js_list([0, 1, 2, 3])


word = ""


def inc_first_char(string: str, index: int):
    global word
    word += string[0]
    word += str(index)


def get_first_char(string: str):
    return string[0]


def test_for_each(names):
    names.for_each(inc_first_char)
    assert word == "C0Q1L2F3"


def test_map(names):
    result = names.map(get_first_char)
    assert result == ["C", "Q", "L", "F"]


def number_sum(acc, num):
    return acc + num


def test_reduce(numbers):
    result = numbers.reduce(number_sum, 10)
    assert result == 16
