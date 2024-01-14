import numpy as np


x = []
a = int(input("Enter the size of the array:"))

for i in range(a):
    x.append(int(input("Enter element:")))
x = np.array(x)

print("Test array:", x)

print("Test if none of the elements of the said array is zero:")
print(np.all(x))
