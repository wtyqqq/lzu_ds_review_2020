def main():
    while True:
        a = input("Please enter a character(q to quit):")
        if a=="q":
            break
        b = int(input("Please enter the number of lines:"))
        c = int(input("Please enter the number of columns:"))
        for i in range(b):
            if (i == 0 or i == (b - 1)):
                print(a * c)
            else:
                print(a, " " * (c - 4), a)


if __name__ == '__main__':
    main()
