from flask import Flask, request, redirect, render_template
from flask_wtf import Form
from wtforms import IntegerField, StringField, SubmitField, SelectField, DecimalField
from wtforms.validators import Required
import pickle
import numpy as np
from sklearn.externals import joblib
from database import models
from sklearn import datasets

app = Flask(__name__)

print('model loading')
model = joblib.load(open('model.pkl', 'rb'))
print('model loaded')

example = np.array([40, 1, 0, 1, 0, 1, 4]).reshape(1, 7)
print(model.predict(example))

@app.route('/')
def hello_world():
    # Landing page for Quinn :)
    return render_template('index.html')


@app.route('/survey', methods=['GET', 'POST'])
def survey():
    if request.method == 'GET':
        return render_template('survey.html')
    form = models.SurveyForm()
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
    app.run(debug=True)
