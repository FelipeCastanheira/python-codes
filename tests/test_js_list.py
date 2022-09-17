from classes.js_list import js_list
import pytest

names = js_list(['Celia', 'Queipe', 'Lelso', 'Fezio'])
word = ''

def inc_first_char(string: str, index: int):
  word += string[0]
  word += str(index)

@pytest.fixture(scope="function")
def test_for_each(word):
  names.for_each(inc_first_char)
  assert word == 'C0Q1L2F3'