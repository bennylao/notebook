def factors():
    for x in range(2000, 4001):
        if x % 9 == 0 and x % 2 == 1:
            print(x)


factors()
