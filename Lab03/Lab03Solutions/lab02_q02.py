def element():
    number = input("Input a number:")
    n = int(number)

    x_n = (n ** 2) + 1

    print(x_n)


element()


def seq():
    number = input("Input a number:")
    n = int(number)

    for x in range(1, n + 1):
        print((x ** 2) + 1)


seq()
