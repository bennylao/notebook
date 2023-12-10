fruits = ['apple', 'banana', 'cherry']
enum_fruits = enumerate(fruits)

next_element = next(enum_fruits)
print(f"Next Element: {next_element}")

fruits = ['apple', 'banana', 'cherry']
for count, item in enumerate(fruits):
    print("count: {:d}; fruit is {:s}".format(count, item))

print("Return type:", type(enum_fruits))
print(list(enumerate(fruits)))

# changing start index to 2 from 0
print(list(enumerate(fruits, 2)))
