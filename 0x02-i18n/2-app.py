#!/usr/bin/env python3

from flask import Flask, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)

class Config:
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)

@babel.localeselector
def get_locale():
    supported_languages = app.config['LANGUAGES']
    return request.accept_languages.best_match(supported_languages)

@app.route('/')
def index():
    return render_template('2-index.html')
