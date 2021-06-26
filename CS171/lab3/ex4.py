def main():
    numbers = [0, 0, 0, 0]
    grades1 = [0, 0, 0, 0]
    grades2 = [0, 0, 0, 0]
    average = [0, 0, 0, 0]
    for x in [0, 1, 2, 3]:
        print("")
        numbers[x] = input("Student {0} number:".format(x + 1))
        grades1[x] = int(input("student {0} grade 1:".format(numbers[x])))
        grades2[x] = int(input("student {0} grade 2:".format(numbers[x])))
        average[x] = (grades1[x] + grades2[x]) / 2
    print("Number   Grade 1   Grade 2   Avg")
    for x in [0, 1, 2, 3]:
        print("{:7}{:7}{:10}{:7}".format(numbers[x], grades1[x], grades2[x], average[x]))


if __name__ == '__main__':
    main()