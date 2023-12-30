import math


def calculate_surface_area():
    radius = float(input("Radius: "))
    height = float(input("Height: "))
    return math.pi * radius ** 2 * height


if __name__ == "__main__":
    calculate_surface_area()
