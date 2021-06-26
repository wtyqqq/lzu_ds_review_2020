def printPascal(n):
    for line in range(1, n + 1):
        C = 1
        for i in range(1, line + 1):
            print(C, end=" ")
            C = int(C * (line - i) / i)
        print("")


if __name__ == '__main__':
    n = 10
    printPascal(n)
