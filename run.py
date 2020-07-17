from flask import Flask, request, redirect, render_template
import numpy as np
import random
from sklearn.externals import joblib

app = Flask(__name__)

print('model loading')
model = joblib.load(open('model.pkl', 'rb'))
print('model loaded')

@app.route('/')
def hello_world():
    # Landing page for Quinn :)
    return render_template('index.html')


@app.route('/survey', methods=['GET', 'POST'], strict_slashes=False)
def survey():
    if request.method == 'GET':
        return render_template('survey.html')
    else:
        skin_type = request.form['skintype']
        budget = request.form['budget']
        label = request.form['product']

        budget = random.randrange(int(budget))
    

        if skin_type == "0":
            # Dry
            example = np.array([int(budget), 0, 1, 0, 0, 0, int(skin_type)]).reshape(1, 7)
            result = model.predict(example)
        elif skin_type == "1":
            # Oily
            example = np.array([int(budget), 0, 0, 0, 1, 0, int(skin_type)]).reshape(1, 7)
            result = model.predict(example)
        elif skin_type == "2":
            # Sensitive
            example = np.array([int(budget), 0, 0, 0, 0, 1, int(skin_type)]).reshape(1, 7)
            print(model.predict(example))
        elif skin_type == "3":
            # Combo
            example = np.array([int(budget), 1, 0, 0, 0, 0, int(skin_type)]).reshape(1, 7)
            result = model.predict(example)
        elif skin_type == "4":
            # normal
            example = np.array([int(budget), 0, 0, 1, 0, 0, int(skin_type)]).reshape(1, 7)
            result = model.predict(example)

        return render_template('recommend.html', product=result[0])

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
    app.run()
