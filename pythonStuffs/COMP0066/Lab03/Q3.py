import math


def calculate_function(y):
    return math.cos(2 * y)


def calculate_first_derivative(y):
    return -2 * math.sin(2 * x)


def calculate_second_derivative(y):
    return -4 * math.cos(2 * y)


if __name__ == "__main__":
    x = math.pi
    ans1, ans2, ans3 = calculate_function(x), calculate_first_derivative(x), calculate_second_derivative(x)
    print(ans1, ans2, ans3)
