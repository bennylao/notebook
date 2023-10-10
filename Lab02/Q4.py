def find_common_elements():
    list_a = input("Enter list A: ").strip("[]").replace(" ", "").split(",")
    list_b = input("Enter list B: ").strip("[]").replace(" ", "").split(",")

    list_common_element = []
    for a in list_a:
        if a in list_b and a not in list_common_element:
            list_common_element.append(a)
    print(list(map(int, list_common_element)))


if __name__ == "__main__":
    find_common_elements()
