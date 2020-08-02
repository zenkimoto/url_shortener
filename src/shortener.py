from math import trunc

URL_SHORTENER_BASE = 62
ASCII_LOWERCASE_A = 97
ASCII_UPPERCASE_A = 65
ASCII_NUMBER_0 = 48

def convert_to_short_url(num):
    # Convert number to base 62 where:
    #   0  => a  (ASCII 97)
    #   10 => k
    #   25 => z
    #   26 => A  (ASCII 65)
    #   51 => Z
    #   52 => 0  (ASCII 48)
    #   61 => 9
    #   62 => ba
    #   63 => bb

    result = ''

    while True:
        rem = num % URL_SHORTENER_BASE

        # Take ASCII # + remainder and concatenate
        if rem < 26:
            result = chr(ASCII_LOWERCASE_A + rem) + result         # a-z
        elif rem < 52:
            result = chr(ASCII_UPPERCASE_A + rem - 26) + result    # A-Z
        else:
            result = chr(ASCII_NUMBER_0 + rem - 52) + result       # 0-9

        num = trunc(num / URL_SHORTENER_BASE)
        if num <= 0:
            break;

    return result

def convert_to_id(string):
    # Converts base 62 string to base 10 int
    #   a  => 0   (ASCII 97)
    #   k  => 10
    #   z  => 25
    #   A  => 26  (ASCII 65)
    #   Z  => 51
    #   0  => 52  (ASCII 48)
    #   9  => 61
    #   ba => 62
    #   bb => 63

    result = 0

    while len(string) > 0:
        ch = string[0]

        if ord('a') <= ord(ch) <= ord('z'):
            result = result * URL_SHORTENER_BASE + ord(ch) - ASCII_LOWERCASE_A
        elif ord('A') <= ord(ch) <= ord('Z'):
            result = result * URL_SHORTENER_BASE + ord(ch) - ASCII_UPPERCASE_A + 26
        else:
            result = result * URL_SHORTENER_BASE + ord(ch) - ASCII_NUMBER_0 + 52

        # Discard first character
        string = string[1:]

    return result