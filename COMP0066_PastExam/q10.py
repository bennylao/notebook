def print_numbers():
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    for i in range(x, y+1):
        is_all_odd = True
        number_str = str(i)
        for digit in number_str:
            if int(digit) % 2 == 0:
                is_all_odd = False

        if is_all_odd is True:
            print(i)

print_numbers()