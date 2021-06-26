MAX_CHAR = 26


def de_duplication(list):
    dedup_list = []
    for word in list:
        if not word in dedup_list:
            dedup_list.append(word)

    return dedup_list


def longest(s1, s2):
    s = s1 + s2
    s = list(s)
    s.sort()
    s = de_duplication(s)
    s = "".join(s)
    return s


if __name__ == '__main__':
    a = "xyaabbbccccdefww"
    b = "xxxxyyyyabklmopq"
    print(longest(a, b))
    a = "abcdefghijklmnopqrstuvwxyz"
    print(longest(a, a))
