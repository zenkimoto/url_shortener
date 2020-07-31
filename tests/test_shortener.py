
from src.shortener import *

def test_convert_single_digit_number_to_short_url():
    assert convert_to_short_url(3) == 'd'

def test_multiple_digit_number_to_short_url():
    assert convert_to_short_url(8000) == 'cfc'

def test_convert_single_character_to_id():
    assert convert_to_id('d') == 3

def test_multiple_character_string_to_id():
    assert convert_to_id('cfc') == 8000