#!/usr/bin/env python3
"""Use user locale"""
from flask import Flask, render_template, request, g
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
        - 6-index.html
    """
    return render_template('6-index.html')

@app.before_request
def before_request():
    user_id = request.args.get('login_as', type=int)
    if user_id in users:
        g.user = users[user_id]
    else:
        g.user = None

@babel.localeselector
def get_locale():
    """Determine best match for supported languages"""
    # Use locale from URL parameter
    if 'locale' in request.args and request.args['locale'] in app.config['LANGUAGES']:
        return request.args['locale']
    # Use locale from user settings
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    # Use locale from request header
    return request.accept_languages.best_match(app.config['LANGUAGES'])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")