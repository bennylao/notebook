
x = int(input("input a first number: "))
y = int(input("input the second number: "))
z = int(input("input the third number: "))

if x > y and x > z:
    if z > y:
        print("The numbers in descending order are:", x, z, y)
    else:
        print("The numbers in descending order are:", x, y, z)

elif y > x and y > z:
    if x > z:
        print("The numbers in descending order are:", y, x, z)
    else:
        print("The numbers in descending order are:", y, z, x)

elif z > x and z > y:
    if x > y:
        print("The numbers in descending order are:", z, x, y)
    else:
        print("The numbers in descending order are:", z, y, x)

else:
     print("You have entered two or even three numbers that are the same. Please try again.")



