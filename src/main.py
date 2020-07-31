from flask import Flask, redirect, request, render_template
from src.shortener import *
from src.db import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test/<int:num>')
def test(num):
    return convert_to_short_url(num)

@app.route('/counter')
def counter():
    num = get_current_id()
    return convert_to_short_url(int(num))

@app.route('/<key>')
def redirect_shorten_url(key):
    return redirect("http://www.example.com")

