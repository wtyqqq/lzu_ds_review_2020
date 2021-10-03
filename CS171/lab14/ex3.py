from string import ascii_lowercase


# function to compute frequencies


def get_freq(test_str):
    # starting at 0 count
    freqs = {char: 0 for char in ascii_lowercase}

    # counting frequencies
    for char in test_str:
        freqs[char] += 1
    return freqs


def check(K, test_str1, test_str2):
    freqs_1 = get_freq(test_str1)
    freqs_2 = get_freq(test_str2)
    res = True
    for char in ascii_lowercase:
        if abs(freqs_1[char] - freqs_2[char]) > K:
            res = False
            break
    return res


if __name__ == '__main__':
    test_str1 = 'aabcdaa'
    test_str2 = "abbaccd"
    K = 2
    print(check(K, test_str1, test_str2))
    test_str1 = 'abcdabcdabcd'
    test_str2 = "efgh"
    K = 2
    print(check(K, test_str1, test_str2))
