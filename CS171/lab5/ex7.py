def find100(sourceList):
    i = 0
    x = None
    while not ((x==100) or (i==len(sourceList))) :
        x=sourceList[i]
        i+=1
    if i == len(sourceList) and  x!= 100:
        print("There is no 100")
    else:
        print("There is a 100 at index no:{0}".format(i))


if __name__ == '__main__':
    testList=[1,2,3,4,5,6,1,1,32,4,3,123,1,100]
    find100(testList)