from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

@app.route('/<hash>')
def handle_hash(hash):
    return redirect("http://www.example.com")