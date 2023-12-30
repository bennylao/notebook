
print("\nPart 1")
print('id of 3 =',id(3))
x=3
print('id of x =',id(x))
y=x
print('id of y =',id(y))
z = 3.0
print('id of z =',id(z))
str1 = "geek"
print(id(str1))
str2 = "geek"
print(id(str2))
print(id(str1) == id(str2))

print("\nPart 2")
print(type(4))
print(type(4.2))
print(type("3"))
print(type( [3, 4, 5] ))
print(type( (3, 4, 5) ))
print(type(type(4)))