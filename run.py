from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/survey', methods=['GET', 'POST'])
# def survey():
#     if request.method == 'GET':
#         return render_template()
#     else:

# @app.route('/recommended')
# def recommended():

# @app.errorhandler(404)
# def not_found(error):
#     return render_template('404.html'), 404
#
# @app.errorhandler(500)
# def not_found(error):
#     return render_template('500.html'), 404

if __name__ == '__main__':
    app.run()
