
from src.shortener import *

def test_convert_zero_to_lowercase_a():
    assert convert_to_short_url(0) == 'a'

def test_convert_two_digit_number_to_short_url():
    assert convert_to_short_url(10) == 'k'

def test_transition_from_lowercase_to_uppercase():
    assert convert_to_short_url(25) == 'z'
    assert convert_to_short_url(26) == 'A'

def test_transition_from_uppercase_to_number():
    assert convert_to_short_url(51) == 'Z'
    assert convert_to_short_url(52) == '0'

def test_transition_from_number_to_two_letter():
    assert convert_to_short_url(61) == '9'
    assert convert_to_short_url(62) == 'ba'
    assert convert_to_short_url(63) == 'bb'

def test_convert_larger_digit_number_to_short_url():
    assert convert_to_short_url(8000) == 'cfc'

def test_convert_a_character_to_0():
    assert convert_to_id('a') == 0

def test_transition_from_lowercase_to_uppercase_to_id():
    assert convert_to_id('z') == 25
    assert convert_to_id('A') == 26

def test_transition_from_uppercase_to_number_to_id():
    assert convert_to_id('Z') == 51
    assert convert_to_id('0') == 52

def test_transition_from_number_to_two_digit_to_id():
    assert convert_to_id('9')  == 61
    assert convert_to_id('ba') == 62
    assert convert_to_id('bb') == 63

def test_multiple_character_string_to_id():
    assert convert_to_id('cfc') == 8000