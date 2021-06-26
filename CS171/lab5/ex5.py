def main():
    lst1 = [111, 32, -9, -45, -17, 9, 85, -10]
    newList = []
    for x in lst1:
        if x > 0:
            newList.append(x)
    print(newList)


if __name__ == '__main__':
    main()
