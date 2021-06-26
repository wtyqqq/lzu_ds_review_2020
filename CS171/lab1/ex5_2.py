
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
    print("count =", len(b), "sum =", total,
          "lowest =", lowest, "highest =", highest,
          "mean =", total / len(b))


if __name__ == '__main__':
    get_number()