from flask import Flask, redirect, request, render_template, make_response, abort
import json
from src.shortener import *
from src.db import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<key>')
def redirect_shorten_url(key):
    url = get_url(key)

    if url == None:
        abort(404, description="Resource not found")

    return redirect(url)


@app.route('/shorten', methods=['POST'])
def shorten_url():
    if 'url' not in request.json:
        abort(400, description="Bad Request")

    url = request.json['url']
    id = get_current_id()
    key = convert_to_short_url(id)
    set_url(key, url)

    return {
        "shortened_url": "/%s" % key
    }