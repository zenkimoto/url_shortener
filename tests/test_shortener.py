
from src.convert import convert_to_short_url

def test_answer():
    assert convert_to_short_url(3) == 'd'

def test_answer2():
    assert convert_to_short_url(8000) == 'cfc'