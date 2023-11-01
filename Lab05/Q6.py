import numpy as np


def check_input_elements():
    element_num = int(input("Enter the size of the array: "))
    array = np.zeros(element_num)
    for i in range(element_num):
        array[i] = input(f"Enter element {i + 1}: ")
    print(array)
    contain_zero = np.all(array)
    print(f"Test if none of the elements of the said array is zero: {contain_zero}")


if __name__ == "__main__":
    check_input_elements()
