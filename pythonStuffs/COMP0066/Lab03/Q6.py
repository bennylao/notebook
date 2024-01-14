def byte_converter(number_of_bytes):
    units = ("B", "KB", "MB", "GB")
    i = 0
    number_of_bytes = int(number_of_bytes)
    for unit in units:
        print(round(number_of_bytes / 2 ** i, 1), unit)
        i += 10


if __name__ == "__main__":
    val = input("Enter the number of number_of_bytes: ")
    byte_converter(val)
