# Python Syntax

## Python Conventions

### Naming Variable
Variable must begin with a letter or underscore. For example, this is not a valid name
```python
56_var
```
Any common unicode character can be used for naming as well.


Python reserved word list cannot be used for naming. To print all the python reserved word list:
```python
import keyword

print(keyboard.kwlist)
```
A better way to list all the keywords
```python
import keyword
help('keywords')
```

### Comments
```python
# Inline comments

"""
Block of comments
"""
```

## Basic Data Types

```int```: Integer<br>
```float```: Float<br>
```complex```: Complex Number<br>
```bool```: Boolean<br>
```str```: String<br>


```int()```, ```float```, ```str()``` convert data types.


### String
```python
print("text")
print('text')
```
If we want to print out the quote symbols:
```{Python}
# Use of different types of quotes
print("This is a 'example' string.")
print('This is a "example" string.')

# Triple quoted string
print('''This string has (') and (").''')
print("""This is the first line.
         This is the second line.
         This is the third line.""")

# Use of excape character
print("This is a \"example\" string.")
```

#### Escape Sequences
```\n``` New line

#### String Operators
```+``` Concatenates strA and strB
```python
strA = "Hello"
strB = "World"

# it prints "HelloWorld"
print(strA + strB)
```
```*``` Duplicates the string n times
```python
str = "Hello"

# it prints "HelloHelloHello"
print(str * 3)
```
```[]``` Slice, return the character at the index<br>
```[:]``` Range Slice, return characters between the given index<br>
```in``` Return ```boolean``` whether the string contains a substring<br>
```not in``` Return ```boolean``` whether the string not contains a substring<br>
```r``` Prevent escape character from being rendered
```python
# it prints \n
print(r"\n")
```
```%``` Format Operator<br>
```python
days = 7

# it prints "A week has 7 days"
print("A week has %d days", %days) 
```

#### String Functions
```python
my_string = "This is a sample string."
my_string.index("sample", 5, 20) # substring, start_pos, end_pos
my_string.index("apple") # Valueerror
```

## Operator
### Assignment Operators
```=```
```+=```


### Logical Operator
```and```
```or```
```not```

### Bitwise Operator
```&``` Binary AND<br>
```python
x = 0b10100
y = 0b01011

x & y
# output is 0
# x & y -> 00000 -> 0
```
```|``` Binary OR<br>
```~```
```^```
```<<```
```>>```

### Membership Operator
```in```
```not in```

### Identity Operator
```is```
```is not```

### Operator Precedence
Table===

### Associativity of Operator of the same priority
if operator has the same priority, it usually evaluated from *LEFT to RIGHT*.
However, for exponent operator ```**```, it is evaluated from *RIGHT to LEFT*.
```python
# LEFT-RIGHT associativity
print(5 + 6 - 7) # output is 4

# RIGHT-LEFT associativity
print(2 ** 3 ** 2) # output is 512
```

## Common Built-in Functions
```type``` Return the type of variable<br>
```id``` Return the id of variable<br>

### If
```if```, ```elif```, ```else```.

Shorthand if
```python
if (x == y): print("x and y are equal")
```
Shorthand if-else
```python
print("true") if x > y else print("false")
```

### For and While

```python
# for-else loop
for condition:
    do something
else:
    suite # only execute when the for loop is completed (without break)
    
# while-else loop
while condition:
    do something
else:
    suite # only execute when the while loop is completed (without break)
```

### List

```mylist.sort()```: sort a list. However, it returns nothing.
```python
mylist.sort(); # sort the list

new_list = mylist.sort() # new_list is none because sort() return nothing
```

### Tuple

```python
# create empty tuple
tup1 = ()

# create tuple with only one element
tup2 = (123,)

# if single element tuple is defined without "," after the element, it will not created it as a tuple
int_tup = (123)
print(type(int_tup)) # type is int
```

### Set
set is an unordered collection with no duplicate elements and set is immutable.
```python
myset = {1, 2, 3}

new_set = set(["a", "b, "c", "b"])
print(new_Set) # it prints {a, b, c} or {c, a, b} or other combinations.
```

#### Set Operator
```python
setA = {1, 2, 3, 4}
setB = {2, 4, 6, 8}

setA & setB # items in both setA and setB
setA | setB # items in either setA and setB
setA - setB # itmes in setA but not in setB
setA ^ setB # items in setA but not in setB AND items in setB but not in setA


```

### Dictionary

```python
mydict = {"key1": value1, "key2", value2}
```

## File
```python
# to open a file
f = open(file, "mode") # default mode is r
```
```file.name```: return the file name<br>
```file.closed```: return True if file is closed<br>
```file.mode```: return the access mode of the file

### Access Mode
```r```: read only<br>
```w```: write only<br>
```a```: append<br>
Example:
```python
lines = ["This is my FIRST line.\n", "This is my SECOND line.\n", "This is my THIR D line.\n"]
f = open("mydata.txt","w") # overwrite the file if the file exists
f.writelines(lines)
f.close()
```

## OOP
Example:
```python
class Person:

    population = 0 # static class attritube
    
    # do something when the object is initialised
    def __init__(self, name):
        """Initialises the data."""
        self.name = name # object attritube
        print("(Initializing {})".format(self.name))
        # When this robot is created, the robot adds to the population
        Robot.population += 1
    
    # define a object method called die
    def die(self):
        """I am dying."""
        print("{} is being destroyed!".format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(Robot.population))
            
    # define a object method called say_hi
    def say_hi(self):
        """ Greeting by the robot """
        print("Greetings, my name is {}.".format(self.name))
```
### Variables
```public```: default variable type, exposed anywhere
```_internalVariable```: declared as a internal variable, but it can still be access outside
```__privateVariable```: cannot be access out of the class

To access the private variable, one way is to declare getter and setter method. (Recommended)

The other way is ```object._class__privateVariable```. However, Name mangling is used to ensure that subclasses don't accidentally override
the private methods and attributes of their superclasses. It's not designed to prevent deliberate access from outside.

Example:
```Python
class Person:
    def __init__(self, age):
        self.__age = age
        
        
p = Person(30)
print(p._Person__age) # access the private variable
```

### Type of Methods
#### Object Methods
Object method is related to the specific object, **it has access to instance or class attributes**
```python
def object_method():
    pass
```
#### Class Methods
Class method is related to the specific class, **it has access to class attributes but not any instance attributes**
```python
@classmethod
def class_method():
    pass
```
#### Static Methods
Static method is related to a class, but **it does not have access to any instance or class attributes**
```python
@staticmethod
def static_method():
    pass
```

## To Do
Dynamic Typed vs Statically Typed
access mode
binary search
mergesort
insertionsort
floyds algorithm
