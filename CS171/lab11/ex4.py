def triangle_area(a, b, c):
    if (a < 0 or b < 0 or c < 0 or (a + b <= c) or (a + c <= b) or (b + c <= a)):
        return False

    s = (a + b + c) / 2

    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area


if __name__ == '__main__':
    print(triangle_area(1, 2, 3))
    print(triangle_area(3, 4, 5))
