#!/usr/bin/env python3
"""forcing locale with URL parameter"""

from flask import Flask, render_template, request
from flask_babel import Babel, _


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
    """

    locale = request.args.get('locale')

    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home():
    """ outputs a simple template to the home page"""

    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)