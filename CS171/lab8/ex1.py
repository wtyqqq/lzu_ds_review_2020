def digital_root(n):
    while n > 9:
        n = sum(int(x) for x in str(n))
    return n


if __name__ == '__main__':
    print(digital_root(16))
    print(digital_root(942))
    print(digital_root(132189))
    print(digital_root(493193))
