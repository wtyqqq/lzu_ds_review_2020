def group_list(test_list):
    res = []
    temp = []
    is_up = True
    if test_list[0] > test_list[1]:
        is_up = False
    for curr, nex in zip(test_list, test_list[1:]):
        temp.append(curr)

        # checking for increasing or decreasing to change list
        if (nex > curr and not is_up) or (nex < curr and is_up):
            res.append(temp)
            temp = []

            # toggling
            is_up = not is_up

    temp.append(nex)
    res.append(temp)
    return res


if __name__ == '__main__':
    test_list = [5, 6, 2, 9, 7, 1, 10, 4, 2, 1, 11, 12, 2]
    print(group_list(test_list))
