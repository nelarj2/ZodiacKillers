from flask import Flask, request, render_template
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from sklearn.svm import LinearSVC
import numpy as np
from flask import Flask, request, jsonify, render_template, url_for, redirect
import pickle
import finalModel
app = Flask(__name__)

df = pd.read_csv("prelim_dataset.csv")
text = df['text'].to_list()
labels = df['Islamophobic?'].to_list()

TFIDF = TfidfVectorizer(ngram_range=(1, 2), stop_words='english')
CLF = LinearSVC(class_weight={0: 1, 1: 5}).fit(
    TFIDF.fit_transform(text), labels)


@app.route('/')
def home():
    return render_template('index.html')

# view detector


@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    input = request.form.get("text")
    predict = TFIDF.transform([input])
    y_pred = CLF.predict(predict)
    return render_template('index.html', prediction_text='Classification Result: {}'.format(y_pred[0]))


# view dashboard
@app.route('/dashboard')
def dashboard():
    '''
    For rendering graphs
    '''
    # getting input data from addDataForm endpoint
    # text = request.args['text']
    # source = request.args['source']
    # label = request.args['label']
    # return render_template('dashboard.html', text=text, source=source, label=label)

    return render_template('dashboard.html')


# view description
@app.route('/description')
def description():
    '''
    For rendering description 
    '''
    return render_template('description.html')

# view form to allow user to add data


@app.route('/addData')
def addData():
    '''
    For adding data 
    '''
    return render_template('addData.html')

# get data entered by user


@app.route('/addDataForm', methods=['POST'])
def addDataForm():
    '''
    For getting data and redirecting
    '''
    text = request.form.get("text")
    source = request.form.get("source")
    label = request.form.get("label")

    # pass data to dashboard endpoint or  pass data to cli.py
    return redirect(url_for('dashboard'))
    # return redirect(url_for('dashboard', text=text, source=source, label=label))


if __name__ == "__main__":
    app.run(debug=True)
