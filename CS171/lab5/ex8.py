def printWeather(sourceList):
    for x in sourceList:
        if x == "sun":
            continue
        print(x)


if __name__ == '__main__':
    weather = ["snow", "rain", "sun", "clouds"]
    printWeather(weather)
