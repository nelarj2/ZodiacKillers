from prometheus_client import start_http_server, Counter

import pandas as pd

start_http_server(9100)

c = Counter('counter', 'Data counter', ['islamophobic', 'source'])

df_twitter = pd.read_csv("TwitterData/prelim_dataset.csv")
df_reddit = pd.read_csv("TwitterData/RedditClean.csv")

t_islamophobic_count = df_twitter.loc[df_twitter["Islamophobic?"]
                                      == 1.0].shape[0]
t_nonislampphobic_count = df_twitter.loc[df_twitter["Islamophobic?"] == 0.0].shape[0]

r_islamophobic_count = df_reddit.loc[df_reddit["islamophobic"] == 1].shape[0]
r_nonislampphobic_count = df_reddit.loc[df_reddit["islamophobic"] == 0].shape[0]
c.labels("yes", "twitter").inc(t_islamophobic_count)
c.labels("no", "twitter").inc(t_nonislampphobic_count)
c.labels("yes", "reddit").inc(r_islamophobic_count)


c.labels("no", "reddit").inc(r_nonislampphobic_count)

while True:
    continue
