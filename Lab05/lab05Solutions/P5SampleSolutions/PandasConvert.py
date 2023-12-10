import pandas as pd

my_dict = dict()
 
size = int(input("Entre the size of the dictionary: "))

for i in range (size):
    key   = input("Enter the key: ")
    value = input("Enter the value: ")
    my_dict[key] = value

print("Original dictionary:")
print(my_dict)

new_series = pd.Series(my_dict)
print("Converted series:")
print(new_series)

