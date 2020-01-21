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


@app.route('/c/<text>')
def c_isfun():
    """ Display c followed by the value of the text variable """
    return "C {}".format(text.replace("_", " "))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
