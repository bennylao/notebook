def print_numbers():
    numbers_list = []
    for i in range(2000, 4001):
        if i % 9 == 0 and i % 2 != 0:
            numbers_list.append(i)
    print(", ".join([str(num) for num in numbers_list]))


if __name__ == "__main__":
    print_numbers()
