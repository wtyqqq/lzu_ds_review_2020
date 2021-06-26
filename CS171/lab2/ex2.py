def main():
    a = int(input("Please enter the number of seconds:"))
    days = int(a / 86400)
    days_left = a % 86400
    hours = int(days_left / 3600)
    hours_left = days_left % 3600
    minutes = int(hours_left / 60)
    seconds = hours_left % 60
    print("{0} seconds correspond to {1} day, {2} hours, {3} minutes and {4} seconds".format(a, days, hours, minutes,
                                                                                             seconds))


if __name__ == '__main__':
    main()

