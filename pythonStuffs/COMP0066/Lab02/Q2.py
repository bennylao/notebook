import math
from typing import final


def calculate_r():
    # Constants
    X = 70
    H = 25

    input_string = input("Enter values of Y:")
    y_list = input_string.split(", ")
    r_list = []
    for y in y_list:
        y = int(y)
        r = int(round(math.sqrt(3 * X * y / H), 0))
        r_list.append(r)
    print(", ".join([str(r) for r in r_list]))


if __name__ == "__main__":
    calculate_r()
