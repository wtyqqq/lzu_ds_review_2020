from collections import defaultdict


def RD(input1):
    res = defaultdict(list)
    for key, val in input1.items():
        for ele in val:
            res[ele].append(key)
    return str(dict(res))


if __name__ == '__main__':
    test_dict = {'gfg': [1, 2, 3], 'is': [1, 4], 'best': [4, 2]}
    print(RD(test_dict))
