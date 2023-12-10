import numpy as np

x = np.array([5, 10, 11, 12, 60, 36, 71])

print("\nInitial NumPy array:",x)

multiple_five = []
multiple_six = []

for i in x:
    if i % 5 == 0:
        multiple_five.append(i)
    if i % 6 == 0:
        multiple_six.append(i)

print(f"List of multiples of 5 in the NumPy array: {multiple_five}")
print(f"List of multiples of 6 in the NumPy array: {multiple_six}")