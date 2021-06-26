def stringOperation3(s):
    s = s.lower()
    dict1 = {}
    for ch in s:
        if ch not in dict1:
            dict1[ch] = 1
        else:
            dict1[ch] += 1
    return dict1


if __name__ == '__main__':
    print(stringOperation3(input("Please enter a string:")))
