delim = '~~~'

def read_file(name):
    tweets = []
    f = open(name, 'r')
    s = ''
    for l in f.readlines():
        if l == delim+'\n':
            tweets.append(s[:-1])
            s = ''
        else:
           s += l
    return tweets

if __name__ == '__main__':
    tweets = read_file('tmp')
    for t in tweets:
        print(t)
