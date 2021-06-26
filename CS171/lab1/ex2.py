def check():
    a = int(input("Please enter the first number:"))
    b = int(input("Please enter the second number:"))
    if a % b:
        print("{0} is not a multiple of {1}".format(a, b))
    else:
        print("{0} is a multiple of {1}".format(a, b))


if __name__ == '__main__':
    check()
