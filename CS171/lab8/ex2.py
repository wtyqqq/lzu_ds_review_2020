def number(bus_stops):
    people = 0
    for items in bus_stops:
        people += items[0]
        people -= items[1]

    return people


if __name__ == '__main__':
    print(number([[10, 0], [3, 5], [5, 8]]))
