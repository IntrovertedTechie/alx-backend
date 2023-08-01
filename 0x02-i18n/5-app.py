#!/usr/bin/env python3
"""Mock logging in"""
from flask import Flask, render_template, g
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)

class Config(object):
    """Available languages class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """GET /
    Return:
        - 5-index.html
    """
    return render_template('5-index.html')

@app.before_request
def before_request():
    user_id = request.args.get('login_as', type=int)
    if user_id in users:
        g.user = users[user_id]
    else:
        g.user = None

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")