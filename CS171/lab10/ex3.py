def queue_time(customers, n):
    tills = [0] * n
    for i in customers:
        tills[0] += i
        tills.sort()
    return max(tills)


if __name__ == '__main__':
    print(queue_time([5, 3, 4], 1))
    print(queue_time([10, 2, 3, 3], 2))
    print(queue_time([2, 3, 10], 2))
