units = ("B", "KB", "MB", "GB")


# KB = 2^10, MB = 2^20, GB = 2^30

def converter(num):
    n = 0
    for x in units:
        num_of_bytes = round(num / (2 ** 10) ** n, 1)
        print(f"{num_of_bytes} {x}")
        n += 1


user_input = int(input("Number of bytes: "))

converter(user_input)
