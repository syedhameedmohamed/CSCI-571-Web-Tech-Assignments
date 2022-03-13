import flask
import pandas as pd
import joblib

# A simple Flask App which takes
# a user's name as input and responds
# with "Hello {name}!"


app = flask.Flask(__name__)

def predict(age, weight):
    clf = joblib.load("/home/syedhame/mysite/static/regr.pkl")
    x = pd.DataFrame([[age, weight]], columns=["Age", "Weight"])
    prediction = clf.predict(x)[0]
    return prediction

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    if flask.request.method == 'POST':
        age = flask.request.form['age']
        weight = flask.request.form['weight']
        message = str(predict(age, weight))

    return flask.render_template('index.html', message=message)

if __name__ == '__main__':
    app.run()
