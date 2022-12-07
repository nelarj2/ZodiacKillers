from flask import Flask, request, render_template
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from sklearn.svm import LinearSVC
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
