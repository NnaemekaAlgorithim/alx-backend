#!/usr/bin/env python3

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)

# Instantiate the Babel object and store it in a module-level variable named babel.
babel = Babel(app)

# Create a Config class for your app.
class Config:
    # Define the available languages as a class attribute.
    LANGUAGES = ["en", "fr"]

# Use the Config class as the configuration for your Flask app.
app.config.from_object(Config)

 # Set Babel's default locale and timezone using configuration options.
BABEL_DEFAULT_LOCALE = 'en'
BABEL_DEFAULT_TIMEZONE = 'UTC'

@app.route('/')
def index() -> str:
    """
    Render the 1-index.html template.

    This route handler renders the index.html template, which displays a simple
    webpage with a title and a header.

    Returns:
        str: HTML content to be displayed in the browser.
    """
    return render_template('1-index.html')

if __name__ == '__main__':
    # Run the Flask application
    app.run()
