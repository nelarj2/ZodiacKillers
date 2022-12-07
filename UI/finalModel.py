# Code adapted from UIUC PS 590: Images and Text as Data
# by Prof. Nora Webb Williams. She adapted from adapted
# from Diyi Yang and crew at Georgia Tech.
from sklearn import metrics
from sklearn.naive_bayes import BernoulliNB
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
import pickle


df = pd.read_csv("prelim_dataset.csv")
# df
# df = pd.read_csv("data.csv")
text = df['text'].to_list()
labels = df['Islamophobic?'].to_list()

tfidf = TfidfVectorizer(ngram_range=(1, 2), stop_words='english')
features = tfidf.fit_transform(text)

# We first split the original data into train and test set
X_train, X_test, y_train, y_test = train_test_split(
    text, labels, random_state=0)

# TODO: More text pre-processing?
# Extract features
tfidf = TfidfVectorizer(ngram_range=(1, 2), stop_words='english')
tfidf.fit(X_train)

X_train_features = tfidf.transform(X_train)
X_test_features = tfidf.transform(X_test)


clf = LogisticRegression(class_weight={0: 0.17, 1: 0.83}).fit(
    X_train_features, y_train)

pickle.dump(clf, open('model.pkl', 'wb'))


# y_pred = clf.predict(X_test_features)
# accuracy_score(y_test, y_pred)

model = pickle.load(open('model.pkl', 'rb'))
# # y_pred = model.predict(X_test_features)
# # acc = accuracy_score(y_test, y_pred)
# # print(acc)


# ex = X_test_features[0]
# print(model.predict(ex))

ex = X_test_features[4]
print(model.predict(ex))
