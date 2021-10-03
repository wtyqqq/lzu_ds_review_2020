def mapping(test_dict1, test_dict2):
    res = {}
    for key, val in test_dict1.items():
        for key1 in val:
            res.setdefault(key, []).extend(test_dict2.get(key1, []))

    return res


if __name__ == '__main__':
    test_dict1 = {"Gfg": [4, 7], "Best": [8, 6], "is": [9, 3]}
    test_dict2 = {6: [15, 9], 8: [6, 3], 7: [9, 8], 9: [10, 11]}
    print(mapping(test_dict1, test_dict2))
