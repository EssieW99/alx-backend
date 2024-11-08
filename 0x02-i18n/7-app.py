#!/usr/bin/env python3
"""inferring appropriate time zone"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import pytz
from pytz.exceptions import UnknownTimeZoneError


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config():
    """ config for the Flask app"""

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    looks at the user request and picks the best language translation to use
    The order of priority should be:
        1. Locale from URL parameters
        2. Locale from user settings
        3. Locale from request header
        4. Default locale
    """

    locale = request.args.get('locale')

    if locale and locale in app.config['LANGUAGES']:
        return locale

    if g.user and g.user.get('locale'):
        user_locale = g.user.get('locale')
        if user_locale and user_locale in app.config['LANGUAGES']:
            return user_locale

    header_locale = request.accept_languages.best_match(
        app.config['LANGUAGES'])
    if header_locale:
        return header_locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """
    returns a user dictionary or None if the ID cannot be found
    or if login_as was not passed.
    """

    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request():
    """ find a user if any, and set it as a global on flask.g.user"""

    g.user = get_user()


@babel.timezoneselector
def get_timezone():
    """
    infers appropriate time zone.
    the order should be:
        1. Find timezone parameter in URL parameters
        2. Find time zone from user settings
        3. Default to UTC
    """

    timezone = request.args.get('timezone')

    if timezone:
        try:
            return pytz.timezone(timezone)
        except UnknownTimeZoneError:
            pass

    if g.user and g.user.get('timezone'):
        user_timezone = g.user.get('timezone')
        try:
            return pytz.timezone(user_timezone)
        except UnknownTimeZoneError:
            pass

    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def home():
    """ outputs a simple template to the home page"""

    return render_template('7-index.html')


if __name__ == '__main__':
    app.run(debug=True)
