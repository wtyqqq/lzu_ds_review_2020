def greeting():
    a = input("Please enter your name:")
    if (a == "Bond") or (a == "bond"):
        print("Welcome on board 007")
    else:
        print("Good morning {0}".format(a))


if __name__ == '__main__':
    greeting()
