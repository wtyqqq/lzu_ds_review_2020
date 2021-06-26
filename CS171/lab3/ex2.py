def main():
    a = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
    b = sorted(a, key=lambda x: x[1],reverse=True)
    print(b)

if __name__ == '__main__':
    main()
