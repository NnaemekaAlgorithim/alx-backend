#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index() -> str:
    """
    Render the 0-index.html template.

    This route handler renders the index.html template, which displays a simple
    webpage with a title and a header.

    Returns:
        str: HTML content to be displayed in the browser.
    """
    return render_template('0-index.html')

if __name__ == '__main__':
    # Run the Flask application
    app.run()
