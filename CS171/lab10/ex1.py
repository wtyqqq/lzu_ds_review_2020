def dig_pow(n, p):
    list1 = [int(i) for i in str(n)]
    list2 = []
    for i in list1:
        list2.append(pow(i, p))
        p += 1
    b = sum(list2)
    return b / n if b % n == 0 else -1


if __name__ == '__main__':
    print(dig_pow(89, 1))
    print(dig_pow(92, 1))
    print(dig_pow(695, 2))
    print(dig_pow(46288, 3))
