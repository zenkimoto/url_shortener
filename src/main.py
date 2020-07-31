from flask import Flask, redirect, request, render_template
from src.bijection import *

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

