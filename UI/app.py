from flask import Flask, request, render_template
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from sklearn.svm import LinearSVC
from flask import Flask, request, render_template, url_for, redirect
from prometheus_client import start_http_server, Counter
import webbrowser

app = Flask(__name__)

start_http_server(9100)

df = pd.read_csv("prelim_dataset.csv")
text = df['text'].to_list()
labels = df['Islamophobic?'].to_list()

TFIDF = TfidfVectorizer(ngram_range=(1, 2), stop_words='english')
CLF = LinearSVC(class_weight={0: 1, 1: 5}).fit(
    TFIDF.fit_transform(text), labels)

TWITTER_COUNT_Y = df.loc[(df["Islamophobic?"] == 1.0) & (df["Source"] == "Twitter")].shape[0]
TWITTER_COUNT_N = df.loc[(df["Islamophobic?"] == 0.0) & (df["Source"] == "Twitter")].shape[0]
REDDIT_COUNT_Y = df.loc[(df["Islamophobic?"] == 1.0) & (df["Source"] == "Reddit")].shape[0]
REDDIT_COUNT_N = df.loc[(df["Islamophobic?"] == 0.0) & (df["Source"] == "Reddit")].shape[0]
YOUTUBE_COUNT_Y = df.loc[(df["Islamophobic?"] == 1.0) & (df["Source"] == "Youtube")].shape[0]
YOUTUBE_COUNT_N = df.loc[(df["Islamophobic?"] == 0.0) & (df["Source"] == "Youtube")].shape[0]

c = Counter('counter', 'Data counter', ['islamophobic', 'source'])
c.labels("yes", "twitter").inc(TWITTER_COUNT_Y)
c.labels("no", "twitter").inc(TWITTER_COUNT_N)
c.labels("yes", "reddit").inc(REDDIT_COUNT_Y)
c.labels("no", "reddit").inc(REDDIT_COUNT_N)
c.labels("yes", "youtube").inc(YOUTUBE_COUNT_Y)
c.labels("no", "youtube").inc(YOUTUBE_COUNT_N)

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
    webbrowser.open_new_tab('http://localhost:3000/d/tjNu-sFVk/islamophobia-dashboard')
    return render_template('index.html')


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
    classification =  "yes"
    if request.form.get("classification") == None:
        classification =  "no"

    c.labels(classification, source.lower()).inc(1)

    # pass data to dashboard endpoint or  pass data to cli.py
    return redirect(url_for('dashboard'))
    # return redirect(url_for('dashboard', text=text, source=source, label=label))


if __name__ == "__main__":
    app.run(port=9123, debug=False)
