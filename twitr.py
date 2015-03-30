from TwitterAPI import TwitterAPI 

from collections import defaultdict
from re import compile

#local file, containing keys
from keys import *

per_search_count    = "50"
num_searches        = 1#6
user                = 'SwiftOnSecurity'

api = TwitterAPI(
        CONSUMER_KEY,
        CONSUMER_SECRET,
        ACCESS_TOKEN_KEY,
        ACCESS_TOKEN_SECRET)

def getTweets():
    requests = []
    r = api.request("statuses/user_timeline", {
        'screen_name': user,
        'count':per_search_count,
        'lang':'en',
        })
    last_id = 0
    for tw in r.get_iterator():
        requests.append(tw['text'])
        last_id = tw['id']
    for i in range(num_searches - 1):
        r = api.request("statuses/user_timeline", {
            'screen_name': user,
            'count':per_search_count,
            'lang':'en',
            'max_id': last_id,
            })
        print(r.response.status_code)
        for tw in r.get_iterator():
            requests.append(tw['text'])
            last_id = tw['id']
    return requests

filtr_re = compile('^\.?(@|RT)')
def filtr(s):
    return filtr_re.match(s) == None

def sanitize(s):
    #TODO: comas, " 
    s = s.strip()
    if not s.endswith('.'):
        s = s + '. '
    s = s.replace('\n', '. ')
    return s


def save_to_file(fname, tweets):
    f = open(fname, 'w')
    for tweet in tweets:
        for t in tweet.split('. '):
            if not t: continue
            if t.endswith('.'):
                t = t[:-1]
            f.write(t + '\n')
    f.close()

if __name__ == "__main__":
    t = getTweets()
    print('len before filter: ', len(t))
    tweets = list(map(sanitize, filter(filtr, t)))
    print('len after filter: ', len(tweets))
    save_to_file('tmp', tweets)

