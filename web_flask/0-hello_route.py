#!/usr/bin/python3
from flask import Flask


app = Flask(__name__)
app-strict_slashes = False

app.run(host='0.0.0.0', port=500)


@app.route('/')
def hbnb():
    return 'Hello HBNB!'
