<<<<<<< Updated upstream
from flask import Flask, request, render_template
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from sklearn.svm import LinearSVC
=======
import numpy as np
from flask import Flask, request, jsonify, render_template, url_for, redirect
import pickle
import finalModel
>>>>>>> Stashed changes
# from flask_bootstrap import Bootstrap

app = Flask(__name__)

df = pd.read_csv("prelim_dataset.csv")
text = df['text'].to_list()
labels = df['Islamophobic?'].to_list()

TFIDF = TfidfVectorizer(ngram_range=(1, 2), stop_words='english')
CLF = LinearSVC(class_weight={0: 1, 1: 5}).fit(TFIDF.fit_transform(text), labels)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    input = request.form.get("fval")
    predict = TFIDF.transform([input])
    y_pred = CLF.predict(predict)
    return render_template('index.html', prediction_text='Classification Result: {}'.format(y_pred[0]))

@app.route('/dashboard')
def dashboard():
    '''
    For rendering graphs 
    '''
    text = request.args['text'] or "Enter data using 'Add Data' tab"
    source = request.args['source'] or "Enter data using 'Add Data' tab"
    label = request.args['label'] or "Enter data using 'Add Data' tab"
    input = "Viewing bashboard"
    return render_template('dashboard.html', text=text, source=source, label=label)


@app.route('/description')
def description():
    '''
    For rendering description 
    '''
    return render_template('description.html')


@app.route('/addData')
def addData():
    '''
    For adding data 
    '''
    return render_template('addData.html')


@app.route('/addDataForm', methods=['POST'])
def addDataForm():
    '''
    For getting data and redirecting
    '''
    text = request.form.get("text")
    source = request.form.get("source")
    label = request.form.get("label")
    return redirect(url_for('dashboard', text=text, source=source, label=label))


if __name__ == "__main__":
    app.run(debug=True)
