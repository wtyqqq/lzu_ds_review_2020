def iq_test(numbers):
    lst = numbers.split()
    evens = []
    odds = []
    for i in lst:
        if int(i) % 2 == 0:
            evens.append(int(i))
        else:
            odds.append(int(i))

    if len(evens) == 1:
        for i in lst:
            if int(i) == evens[0]:
                return lst.index(i) + 1

    if len(odds) == 1:
        for i in lst:
            if int(i) == odds[0]:
                return lst.index(i) + 1


if __name__ == '__main__':
    print(iq_test("2 4 7 8 10"))
    print(iq_test("1 2 1 1"))
    print(iq_test("1 2 2"))
