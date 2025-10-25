from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/about', strict_slashes=False)
def about():
    return render_template('about.html')


@app.route('/games', strict_slashes=False)
def games():
    return render_template('games.html')


handler = app
