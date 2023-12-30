import math as m


def formula(X=70, H=25):
    n = input("What values of Y would you like to use: ")

    str_values = n.split(",")

    int_values = []

    for y in str_values:
        Y = int(y)
        int_values.append(Y)

    int_results = []

    for a in int_values:
        R = m.sqrt((3 * X * a) / H)
        r = str(round(R))
        int_results.append(r)

    answers = ",".join(int_results)
    print(answers)


formula()