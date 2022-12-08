#!C:\Users\narjum2\AppData\Local\Programs\Python\Python310\python.exe


import cgitb
import cgi
import pandas as pd
from prometheus_client import start_http_server, Counter
form = cgi.FieldStorage()
# to get the data from fields
text = form.getvalue('text')
source = form.getvalue('source')
label = form.getvalue('label')


print("Content-type:text/html\n")
print("<html>")
print("<head>")
print("<title>First CGI Program</title>")
print("</head>")
print("<body>")
print("<h2>Text: %s Source: %s Label: %s</h2>"
      % (text, source, label))
print("</body>")
print("</html>")

# PASS INTO cli.py file


# start_http_server(9100)


# c = Counter('counter', 'Data counter', ['islamophobic', 'source'])

# df_twitter = pd.read_csv("TwitterData/prelim_dataset.csv")
# df_reddit = pd.read_csv("TwitterData/RedditClean.csv")

# t_islamophobic_count = df_twitter.loc[df_twitter["Islamophobic?"]
#                                       == 1.0].shape[0]
# t_nonislampphobic_count = df_twitter.loc[df_twitter["Islamophobic?"] == 0.0].shape[0]

# r_islamophobic_count = df_reddit.loc[df_reddit["islamophobic"] == 1].shape[0]
# r_nonislampphobic_count = df_reddit.loc[df_reddit["islamophobic"] == 0].shape[0]
# c.labels("yes", "twitter").inc(t_islamophobic_count)
# c.labels("no", "twitter").inc(t_nonislampphobic_count)
# c.labels("yes", "reddit").inc(r_islamophobic_count)


# c.labels(label, source).inc(label)

# while True:
#     continue
