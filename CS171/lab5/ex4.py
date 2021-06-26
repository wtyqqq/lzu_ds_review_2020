from math import floor

def thedecimal(number):
    a = floor(number)
    b = number - a
    if b:
        return b
    else:
        return "INTEGER"


if __name__ == '__main__':
    print(thedecimal(float(input())))
