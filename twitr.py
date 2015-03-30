from TwitterAPI import TwitterAPI 

from collections import defaultdict
from re import compile

#local file, containing keys
from keys import *

per_search_count    = "100"
user                = 'SwiftOnSecurity'

line_split          = "~~~"

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
    for tw in r.get_iterator():
        requests.append(tw['text'])
    return requests

filtr_re = compile('^\.?(@|RT)')
def filtr(s):
    return filtr_re.match(s) == None

if __name__ == "__main__":
    t = getTweets()
    print('len before filter: ', len(t))
    tweets = list(filter(filtr, t))
    print('len after filter: ', len(tweets))
    for t in tweets:
        print(t)
        print('~')

