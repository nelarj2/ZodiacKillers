import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import finalModel
# from flask_bootstrap import Bootstrap

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    # input = request.form.get("fval")
    # print(input)

    # predict = finalModel.tfidf.transform([input])
    # y_pred = clf.predict(predict)
    # print(y_pred[0])

    # Hard code data
    x = finalModel.ex

    prediction = model.predict(x)
    # output = round(prediction[0], 2)
    # print(x.toarray())

    return render_template('index.html', prediction_text='Classification Result: {}'.format(prediction[0] == 1))

    # return render_template('index.html', prediction_text='Classification result: {}'.format(prediction), url="https://grafana.com/static/assets/img/blog/dual_axis_graph3.png")


@app.route('/dashboard')
def dashboard():
    '''
    For rendering graphs 
    '''
    input = "Viewing bashboard"
    return render_template('dashboard.html', text=input)


@app.route('/description')
def description():
    '''
    For rendering description 
    '''
    return render_template('description.html')


if __name__ == "__main__":
    app.run(debug=True)
