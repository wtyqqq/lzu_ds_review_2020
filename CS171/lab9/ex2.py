def nb_year(p0, per, aug, p):
    year = 0;
    while p0 < p:
        year += 1
        p0 *= (1 + per / 100)
        p0 += aug
    return year

if __name__ == '__main__':
    print(nb_year(1500, 5, 100, 5000))
    print(nb_year(1500000, 2.5, 10000, 2000000))