myList = ['X',34.7, 9, ["6"], .65, "Hello", (44,5), [1, 2, "ABC"], ("V", "W")]

tuple_list = []
for item in myList:
    if isinstance(item, tuple):
        tuple_list.append(item)

print(tuple_list)