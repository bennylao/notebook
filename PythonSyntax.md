# Python Syntax

## Python Conventions

### Naming Variable
Variable must begin with a letter or underscore. For example, this is not a valid name
```python
# This is not a valid name
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

```int```: Integer <br>
```float```: Float <br>
```complex```: Complex Number <br>
```bool```: Boolean <br>
```str```: String <br>

```python
a = 10 # integer
b = 5.1 # float

# complex number
import cmath
z = 5+3j
print(z.real) # real part of complex number
print(z.imag) # imaginary part of complex number
print(cmath.sqrt(z)) # use of mathematical function on complex number

c = True # boolean
d = "string" # string
```

```int(var)```, ```float(var)```, ```str(var)``` convert data types.


### String
```python
print("text")
print('text')
```
If we want to print out the quote symbols:
```python
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

#### Escape Characters
```\n``` New line

#### String Operators
```+```: Concatenates strA and strB <br>
```*```: Duplicates the string n times <br>
```str[i]```: Returns the characters from the index at i <br>
```str[i:j]```: Returns the characters from the index in the range i to j where j is excluded <br>
```str_a in str_b```: Returns True if str_a exist in str_b <br>
```a not in str_b```: Returns True if str_a does not exist in str_b <br>
```r"\n"```: Prevents escape characters from being rander
```"{:d}".format(integer)```: The string formatting operator

```python
print("I am " + "string")
print("n" * 10)

str_a = "apple"
str_b = "apple bannana"

print(str_a[0])
print(str_a[0:3])
print(str_a[1:])
print(str_a[:])

print(str_a in str_b)
print(str_a not in str_b)

print("First Line\nSecond Line")
print(r"First Line\n Still First Line")

num = 7
print("There are %d days in a week" %num)
```
#### String Formatting Operators
```{:d}```: Integer <br>
```{:s}```: String <br>
```{:f}```: Floating point numbers <br>
```{:.2f}```: Floating point numbers with fixed amount of decimal places <br>
```{:b}```: Integer in binary (2-bit) <br>
```{:o}```: Integer in octal (8-bit) <br>
```{:x}```: Integer in hex (16-bit) <br>

```python
print("String: {:s}; Integer: {:d}".format("Hello", 100))
print("r is {!r}, s is {!s}".format("test1", "test2"))
print("binary: {:b}".format(10))
print("d: {0:d} {0:x}".format(10))
print("{:.3f}".format(123.12345))
print("{!r}".format("10"))

print('{:<30}'.format('left aligned'))
"""left aligned                  """
print('{:>30}'.format('right aligned'))
"""                 right aligned"""
print('{:^30}'.format('centered'))
"""           centered           """
print('{:*^30}'.format('centered'))  # use '*' as a fill char
"""***********centered***********"""
```

#### F-Strings
```f"string {var}"```: easier F-String
```python
num = 7
print(f"There are {num} days in a week")
```

#### String Functions
```python
my_string = "This is a sample string."
my_string.index("sample", 5, 20) # substring, start_pos, end_pos
my_string.index("apple") # Valueerror
```

## Operator

### Arithmetic Operators (Mathematical Operators)
```+```: addition
```-```: subtraction
```*```: multiplication
```/```: division
```%```: modulus
```**```: exponentiation
```//```: floor division

### Logical Operator
```and```
```or```
```not```

### Bitwise Operator
```&```: Bitwise AND <br>
```|```: Bitwise OR <br>
```^```: Bitwise XOR <br>
```~```: Bitwise NOT <br>
```<<```: Bitwise left shift <br>
```>>```: Bitwise right shift <br>
```python
x = 0b10100
y = 0b01011

print("x & y =", x & y)
# output is 0
# x & y -> 00000 -> 0

print("x | y =", x | y)
# output is 31

print("x ^ y =", x ^ y)
# output is 31
# 1 != 0 --> 1
# 1 == 1 --> 0
# 0 == 0 --> 0

a = 0b00111
b = 3
print(~a)
print(~b)
# output is 31

print(a >> 1)
print(b << 2)
```


### Membership Operator
```in```
```not in```

### Identity Operator
```is```
```is not```

### Operator Precedence
![screenshot](docs/assets/operator_precedence.png)

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
```type(var)``` Return the type of variable<br>
```id(var)``` Return the id of variable<br>

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

## Data Structures

### List

```len(my_list)```: Returns length of the list <br>
```my_list.append(item)```: Add item to the end of the list <br>
```my_list.extend(item1, item2)```: Add multiple items to the end of the list <br>
```my_list.insert(i, item)```: Insert item into the position at index i <br>
```my_list.remove(item)```: Remove item from the list <br>
```my_list.pop(i)```: Remove item from the position at index i, if no index is given, the last item will be removed <br>
```my_list.index(item)```: Return index of an item in the list <br>
```my_list.reverse()```: Reverse a list <br>
```my_list.count()```: Count the number of item in list <br>
```my_list.sort()```: Sort my_list. Note that it returns NOTHING! <br>
```python
mylist.sort(); # sort the list

new_list = mylist.sort() # new_list is none because sort() return nothing

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[:4])
print(numbers[:-4])
print(numbers[3:])
print(numbers[::-1])
print(numbers[::-2])
# List[start:stop:step]
"""
If start and stop are omitted, slicing goes from first to last with a positive step, 
and last to first with a negative step.
"""
print(numbers[1:8:2])
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
```_internalVariable```: declared as an internal variable, but it can still be access outside
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

## Package and Module

```Python
---pkg_root
    --pkg1
        --module1.py
        --module2.py
    --pkg2
        --module1.py
        --module.py
```

### __init__.py

```__init__.py``` is used to mark the directory as a package.


## Logging
The is five levels of logging.
```python
import logging

# logging levels low to high
logging.debug("debug message")
logging.info("info message")
logging.warning("warning message")
logging.error("error message")
logging.critical("critical message")
```

```python
import logging

# the basic level of logging is WARNING
# to set the level of logging lower or higher, use basicConfig(level = {level})
logging.basicConfig(level=logging.DEBUG)
```

```python
import logging

# set the basic logging level
# determine where the logs go
# file open mode
# format of the log
logging.basicConfig(level=logging.DEBUG, 
                    filename = 'output.log', 
                    filemode ='w', 
                    format = '%(module)s - %(levelname)s - %(message)s')

# testing
logging.warning("This is a warning message")
```

## Other Functions
```enumerate()```: Create enumerate object of a list

```python
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
```


## To Do
Dynamic Typed vs Statically Typed
access mode
binary search
mergesort
insertionsort
floyds algorithm
