def encrypt(inp):
    str1 = ''
    for i in inp:
        if str.isalpha(i):
            if i == 'z':
                str1 += 'A'
            else:
                str1 += str.swapcase(chr(ord(i) + 1))
        else:
            str1 += i
    return str1


if __name__ == '__main__':
    print(encrypt('.I love LanZhou University.'))
