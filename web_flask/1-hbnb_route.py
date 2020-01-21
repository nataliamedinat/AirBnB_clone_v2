#!/usr/bin/python3
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb():
    """ Flask web app """
    return 'Hello HBNB!'


@app.route('/hbnb')
def display_hbnb():
    """ Flask """
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)