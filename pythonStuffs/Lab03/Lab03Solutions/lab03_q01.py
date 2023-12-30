import math as m


def surface_area():
    r = input("What is the radius of your cylinder?: ")
    R = int(r)

    h = input("And what is the height of your cylinder?: ")
    H = int(h)

    s_area = R * H * m.pi

    x = round(s_area, 2)

    print(f"The Surface Area of your cylinder of radius {R} and height {H} is {x} units squared.")


surface_area()
