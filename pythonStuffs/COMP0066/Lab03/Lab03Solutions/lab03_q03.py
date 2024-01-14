import math as m


def trig(x):
    x_1 = m.cos(2 * x)
    x_2 = -2 * (m.sin(2 * x))
    x_3 = -4 * (m.cos(2 * x))

    print(f"{x_1} , {x_2} , {x_3}")


trig(m.pi)
