import string


def main():
    input_words = input("Please enter a sentence:")
    a = input_words.strip(string.punctuation)
    b = list(a.split(" "))
    length = len(b)
    a = ""
    for x in range(len(b)):
        c = b[x]
        if len(c) > len(a):
            a = c
    print("The sentence has {0} sentences and the longest word is {1}.".format(length, a))


if __name__ == '__main__':
    main()
