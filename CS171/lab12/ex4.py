def findMinSum(num):
    sum = 0
    i = 2
    while (i * i <= num):
        while (num % i == 0):
            sum += i
            num /= i
        i += 1
    sum += num
    return sum


if __name__ == '__main__':
    a = 12
    b = 105
    print(findMinSum(a))
    print(findMinSum(b))