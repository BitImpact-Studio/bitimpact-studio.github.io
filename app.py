from flask import Flask, render_template
from flask_frozen import Freezer


app = Flask(__name__)
freezer = Freezer(app)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/about', strict_slashes=False)
def about():
    return render_template('about.html')


@app.route('/games', strict_slashes=False)
def games():
    return render_template('games.html')


if __name__ == '__main__':
    freezer.freeze()
