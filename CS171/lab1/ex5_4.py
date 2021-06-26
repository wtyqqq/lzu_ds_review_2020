#!/usr/bin/env python3

import random
import sys


def randomSentence():
    l = 5
    if len(sys.argv) > 1:
        try:
            t = int(sys.argv[1])
            if 1 <= t <= 10:
                l = t
            else:
                print("lines must be 1-10 inclusive")
        except ValueError:
            print("usage: badpoetry.py [lines]")
    articles = ["the", "a", "another", "her", "his"]
    subjects = ["cat", "dog", "horse", "man", "woman", "boy", "girl"]
    verbs = ["sang", "ran", "jumped", "said", "fought", "swam", "saw",
             "heard", "felt", "slept", "hopped", "hoped", "cried",
             "laughed", "walked"]
    adverbs = ["loudly", "quietly", "quickly", "slowly", "well", "badly",
               "rudely", "politely"]

    for x in range(l):
        a = random.choice(articles)
        b = random.choice(subjects)
        c = random.choice(verbs)
        d = random.randint(0, 1)
        if d:
            print(a, b, c)
        else:
            e = random.choice(adverbs)
            print(a, b, c, e)


if __name__ == '__main__':
    randomSentence()
