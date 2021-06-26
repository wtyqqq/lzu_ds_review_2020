def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


def calarea():
    pi = 3.1416
    b = input("Please enter the radius of the circle:")
    if is_number(b):
        a = float(b)
        print("perimeter = {0}".format(2 * pi * a))
        print("Area = {0}".format(pi * a * a))
    else:
        print("You have not inserted a valid number!")
    return 0


if __name__ == '__main__':
    calarea()
