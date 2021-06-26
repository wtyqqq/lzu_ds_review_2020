from typing import List


def bucket_sort(arr: List[int]):
    min_num = min(arr)
    max_num = max(arr)
    bucket_range = (max_num - min_num) / len(arr)
    count_list = [[] for i in range(len(arr) + 1)]
    for i in arr:
        count_list[int((i - min_num) // bucket_range)].append(i)
    arr.clear()
    for i in count_list:
        for j in sorted(i):
            arr.append(j)


def get_number():
    number = 0
    lowest = None
    highest = None
    total = 0
    b = []
    while True:
        try:
            a = input("enter a number or Enter to finish:")
            if not a:
                break
            a = int(a)
            b.append(a)
            number += 1
            total += a
            if lowest is None or lowest > a:
                lowest = number
            if highest is None or highest < a:
                highest = number
        except ValueError as err:
            print(err)

    print("numbers:", b)
    bucket_sort(b)
    if len(b) % 2:
        n = int((len(b)+1)/2)
    else:
        n = int(len(b)/2)
    mid = b[n]
    print("count =", len(b), "sum =", total,
          "lowest =", lowest, "highest =", highest,
          "mean =", total / len(b),"mid=",mid)


if __name__ == '__main__':
    get_number()
