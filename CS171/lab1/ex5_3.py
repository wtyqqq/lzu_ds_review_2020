#!/usr/bin/env python3

import random


def randomSentence():
    articles = ["the", "a", "another", "her", "his"]
    subjects = ["cat", "dog", "horse", "man", "woman", "boy", "girl"]
    verbs = ["sang", "ran", "jumped", "said", "fought", "swam", "saw",
             "heard", "felt", "slept", "hopped", "hoped", "cried",
             "laughed", "walked"]
    adverbs = ["loudly", "quietly", "quickly", "slowly", "well", "badly",
               "rudely", "politely"]

    for x in range(5):
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
