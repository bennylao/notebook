import sys


filename = input("Enter the list of filenames: ")
f = open(filename, "r")
print(f.readlines())
