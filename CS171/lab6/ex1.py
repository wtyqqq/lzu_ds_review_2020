def divide(num1, num2):
    count = 0
    while num1 >= num2:
        num1 -= num2
        count += 1
    print("{count},{num1}".format(**locals()))


if __name__ == '__main__':
    divide(10,3)
