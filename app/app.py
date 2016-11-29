"""Main application entrypoint."""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    """Index handler."""
    return 'Hello, world!'


@app.route('/<name>')
def greet(name):
    """Greet handler."""
    return 'Hello, {0}!'.format(name)


if __name__ == '__main__':
    app.run(port=5000)
