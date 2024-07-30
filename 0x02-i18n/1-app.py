from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

class Config:
    """
    configure languages, default locale, and timezone
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'




@app.route('/')
def index():
    """ renders the index.html template"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)