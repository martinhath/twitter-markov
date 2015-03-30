from collections import defaultdict
from random import random

delim = '~~~'

def read_file(name):
    tweets = []
    f = open(name, 'r')
    s = ''
    for l in f.readlines():
        l = l.strip()
        tweets.append(l)
    return tweets

"""
returns a dict, such that d['word'] is a function
that takes a number [0,1], and returns a word.
"""

def build_markov(lines):
    dct = defaultdict(str)
    for line in lines:
        words = line.split()
        pairs = list(zip(words, words[1:]))
        for p in pairs:
            if not dct[p[0]]:
                dct[p[0]] = defaultdict(int)
            dct[p[0]][p[1]] += 1
    # Now `dct` is a map string -> dict, where
    # each element is a dict of words with frequencies.
    dc = {}
    def helper(word, d):
        tot_f = sum(d.values())
        f0 = 0
        pairs = []
        for (next, freq) in d.items():
            f = float(freq)/tot_f
            pairs.append((next, f + f0))
            f0 += f
        print(word, pairs)
        def f(i):
            for (w, f) in pairs:
                if f >= i:
                    return w
        dc[word] = f
    for (word, d) in dct.items():
        helper(word, d)
    return dc

        


if __name__ == '__main__':
    tweets = read_file('tmp2')
    d = build_markov(tweets)
    for i in range(20):
        print(d['a'](random()))
