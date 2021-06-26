def is_valid_IP(string):
    temp = string.split('.')
    if len(temp) != 4:
        return False
    for str in temp:
        a = 0
        if str.isdigit() == False:
            return False
        a = int(str)
        if str.find('0') == 0 and a != 0:
            return False
        if a < 0 or a > 255:
            return False
    return True


if __name__ == '__main__':
    print(is_valid_IP("1.2.3.4"))
    print(is_valid_IP("123.45.67.89"))
    print(is_valid_IP("1.2.3"))
    print(is_valid_IP("1.2.3.4.5"))
    print(is_valid_IP("123.045.067.089"))