from flask import render_template
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    # Landing page for Quinn :)
    return render_template('index.html', title='Home')


@app.route('/survey/')
def survey():
    return render_template('survey.html', title='Home')


if __name__ == '__main__':
    app.run()
