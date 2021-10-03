def subtract(K, test_list):
    res = []
    for ele in test_list:
        str_ele = str(ele)
        new_ele = int(''.join([str(max(0, int(el) - K)) for el in str_ele]))
        res.append(new_ele)
    return res


if __name__ == '__main__':
    test_list = [2345, 8786, 2478, 8664, 3568, 28]
    print(subtract(4, test_list))
