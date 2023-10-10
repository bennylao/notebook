# UCL_CS

## Python Conventions

### Naming Variable

Variable must begin with a letter or underscore. For example, this is not a valid name
```
56_var
```
Any common unicode character can be used for naming as well.


Python reserved word list cannot be used for naming. To print all the python reserved word list:
```
import keyword
print(keyboard.kwlist)
```
A better way to list all the keywords
```
import keyword
help('keywords')
```

### Comments
```
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
```
print("text")
print('text')
```
If we want to print out the quote symbols:
```
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
```
strA = "Hello"
strB = "World"

# it prints "HelloWorld"
print(strA + strB)
```
```*``` Duplicates the string n times
```
str = "Hello"

# it prints "HelloHelloHello"
print(str * 3)
```
```[]``` Slice, return the character at the index<br>
```[:]``` Range Slice, return characters between the given index<br>
```in``` Return ```boolean``` whether the string contains a substring<br>
```not in``` Return ```boolean``` whether the string not contains a substring<br>
```r``` Prevent escape character from being rendered
```
# it prints \n
print(r"\n")
```
```%``` Format Operator<br>
```
days = 7

# it prints "A week has 7 days"
print("A week has %d days", %days) 
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
```
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
```
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
```
if (x == y): print("x and y are equal")
```
Shorthand if-else
```
print("true") if x > y else print("false")
```

### For and While

```
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

## To Do
Dynamic Typed vs Statically Typed
binary search
mergesort
insertionsort
floyds algorithm
