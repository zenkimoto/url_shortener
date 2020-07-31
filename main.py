from flask import Flask, redirect, request, render_template
from math import trunc

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test/<int:num>')
def test(num):
    return biject_number(num)

@app.route('/<key>')
def handle_shorten_url(key):
    return redirect("http://www.example.com")

def biject_number(num):
    # a - 97 - 122 => 26
    # A - 65 - 90 => 26
    # 0 - 48 - 57 => 10
    # a - 97 - 122
    # A - 65 - 90
    # 0 - 48 - 57
    # This function will perform a bijection from a number to a string 0-9a-zA-Z
    result = ''

    while True:
        rem = num % 62

        if rem < 26:
            result = chr(97 + rem) + result         # a-z
        elif rem < 52:
            result = chr(65 + rem - 26) + result    # A-Z
        else:
            result = chr(48 + rem - 52) + result    # 0-9

        num = trunc(num / 62)
        if num <= 0:
            break;

    return result

def biject_string(string):
    result = 0

    while len(string) > 0:
        ch = string[0]

        if ord('a') <= ord(ch) <= ord('z'):
            result = result * 62 + ord(ch) - 97
        elif ord('A') <= ord(ch) <= ord('Z'):
            result = result * 62 + ord(ch) - 65
        else:
            result = result * 62 + ord(ch) - 48

        string = string[1:]

    return result