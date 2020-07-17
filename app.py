from flask import Flask, request, redirect, render_template
from database import db
from database import models

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Landing page for Quinn :)
    return render_template('index.html')


@app.route('/survey', methods=['GET', 'POST'])
def survey():
    if request.method == 'GET':
        return render_template('survey.html')
    form = models.SurveyForm(request.form)
    if request.method == 'POST':
        if form.validate():
            print('Done!')
        return render_template('recommend.html')

@app.route('/recommend')
def recommend():
    return render_template('recommend.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def not_found(error):
    return render_template('500.html'), 404

if __name__ == '__main__':
    db.initialize_db(app)
    app.run(debug=True)
