"""Main application entrypoint."""

import random

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    """Index handler."""
    return 'Welcome to the math machine!'


@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    """Addition handler."""
    return str(a + b)


@app.route('/subtract/<int:a>/<int:b>')
def subtract(a, b):
    """Subtraction handler."""
    return str(a - b)


@app.route('/multiply/<int:a>/<int:b>')
def multiply(a, b):
    """Multiplication handler."""
    return str(a * b)


@app.route('/divide/<int:a>/<int:b>')
def divide(a, b):
    """Floor division handler."""
    if b == 0:
        return 'You cannot divide by 0'
    return str(a / b)


@app.route('/modulo/<int:a>/<int:b>')
def modulo(a, b):
    """Modulo handler."""
    return str(a % b)


@app.route('/random')
def random_num():
    """Random number handler."""
    return str(random.random())


@app.route('/random/<int:max_boundary>')
def random_int(max_boundary):
    """Random integer handler."""
    return str(random.randint(1, max(1, max_boundary)))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
