def str_mat(input1):
    res = []
    N = 0
    while N != len(input1):
        temp = ''
        for idx in input1:
            try:
                temp = temp + idx[N]
            except IndexError:
                pass
        res.append(temp)
        N = N + 1

    res = [ele for ele in res if ele]
    return str(res)


if __name__ == '__main__':
    a = [["Gfg", "good"], ["is", "for"]]
    b = [['Gfg', 'good'], ['is', 'for'], ['Best']]
    print(str_mat(a))
    print(str_mat(b))
