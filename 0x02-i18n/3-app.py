#!/usr/bin/env python3
"""Parametrize templates"""
from flask import Flask, render_template
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)

class Config(object):
    """Available languages class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)

@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """GET /
    Return:
        - 3-index.html
    """
    return render_template('3-index.html', home_title=_("Welcome to Holberton"), home_header=_("Hello world!"))

@babel.localeselector
def get_locale():
    """Determine best match for supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")