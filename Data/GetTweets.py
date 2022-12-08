import requests
import os
import pandas as pd
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'

bearer_token = os.getenv('BEARER')

search_url = "https://api.twitter.com/2/tweets/search/recent"

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
query_params = {'query': '(#islam OR #muslim) -is:retweet lang:en','tweet.fields': 'author_id,created_at'}


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    # print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


json_response = connect_to_endpoint(search_url, query_params)

df = pd.DataFrame()
query_params['next_token'] = json_response['meta']['next_token']
json_response = connect_to_endpoint(search_url, query_params)
meta_data = json_response['meta']
count = meta_data['result_count']
for tweet in json_response['data']:
    new_row = { 'author_id': tweet['author_id'],
                    'created_at': tweet['created_at'],
                    'id': tweet['id'],
                    'text': tweet['text']}
    df = pd.concat([df, pd.DataFrame.from_records([new_row])])

while ('next_token' in meta_data and count < 1000):
    query_params['next_token'] = json_response['meta']['next_token']
    json_response = connect_to_endpoint(search_url, query_params)
    count += meta_data['result_count']
    for tweet in json_response['data']:
        new_row = { 'author_id': tweet['author_id'],
                        'created_at': tweet['created_at'],
                        'id': tweet['id'],
                        'text': tweet['text']}
        df = pd.concat([df, pd.DataFrame.from_records([new_row])])
df['author_id'] = df['author_id'].astype(str)
df['id'] = df['id'].astype(str)
df.to_excel('./TwitterData/tweets.xlsx', index=False)