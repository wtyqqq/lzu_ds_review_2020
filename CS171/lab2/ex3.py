def main():
    a = input("Please enter a string:")
    if a == a[::-1]:
        print("{0} is a palindrome".format(a))
    else:
        print("{0} is not a palindrome".format(a))


if __name__ == '__main__':
    main()