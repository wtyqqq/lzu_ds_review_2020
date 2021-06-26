def telenum(l1):
    l1 = "".join('%s' %id for id in l1)
    x = "(" + l1[0:3] + ") " + l1[3:6] + "-" + l1[6:]
    return x


if __name__ == '__main__':
    print(telenum([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
