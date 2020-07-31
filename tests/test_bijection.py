
from src.bijection import biject_number

def test_answer():
    assert biject_number(3) == 'd'

def test_answer2():
    assert biject_number(8000) == 'cfc'