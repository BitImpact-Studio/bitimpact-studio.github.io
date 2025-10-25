from flask import Flask, render_template
from flask_frozen import Freezer

build = False

app = Flask(__name__)

if build:
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
    if not build:
        app.run(debug=True)
    else:
        freezer.freeze()
