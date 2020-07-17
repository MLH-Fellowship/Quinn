from flask import Flask, request, redirect, render_template, session, url_forß
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
def home():
    # Landing page for Quinn :)
    return render_template('index.html')


@app.route('/survey', methods=['GET', 'POST'])
def survey():
    print(session)
    if request.method == 'GET':
        return render_template('survey.html')
        
    form = models.SurveyForm(csrf_enabled=False)
    if request.method == 'POST':
        if form.validate():
            session['price'] = form.q3.data
            session['skin_type'] = form.q1.data
            session['product_type'] = form.q_2.data

            survey_instance= [(session['price']), (session['skin_type']), (session['product_type'])]

        #TODO: add lines to return model recommendations

            return redirect(url_for('home')
        return render_template('recommend.html', form=form, **session)

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
