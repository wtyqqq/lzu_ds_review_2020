def list_max(int_list):
    a = int_list.pop()
    while len(int_list) >= 1:
        b = int_list.pop()
        if a < b:
            a = b
    return a


if __name__ == '__main__':
    print(list_max([1, 2, 8, 3, 10, 5]))
