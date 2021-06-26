def returnType(sourceList):
    resultList = []
    for x in sourceList:
        resultList.append(type(x))
    return resultList


if __name__ == '__main__':
    lst1 = [3.14, 66, "Teddy Bear", True, [], {}]
    print(returnType(lst1))
