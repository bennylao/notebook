# Miranda Notes

SSH into UCL Cs
```temrinal
ssh chonlao@knuckles.cs.ucl.ac.uk
```

Access Miranda
```terminal
mira
```

## Miranda Instructions

Select vim to be the editor
```miranda
/editor vim
```

Manual
```miranda
/man
```

Help
```miranda
/h
```

Quit Miranda
```miranda
/q
```

Edit Script
```miranda
/e
```

Load New Script
```miranda
/f filename.m || load filename.m from current directory
```

Quit without saving
```miranda
/q!
```

Save
```miranda
:w
```

Save and quit
```miranda
:wq
```

## Basics

- Names must start with lowercase
- Name is given to a value rather than giving a name to a memory location
- Due to **referential transparency**, the value of name is constant. 
Hence, the result of a given expression is the same whenever it appears in a program.
- Same name cannot be used twice


### Type

- Numbers
- Characters
- Text
- Truth values
- Functions


Query type of value
```miranda
34 :: || return num

(34, True) :: || return type of (num, bool)
```

Query input type and output type of function
```miranda
twice x = x * 2 || if this function is defined in script
```
```miranda
twice :: || num_>num
```


#### Numbers (num) 

##### Built-in Operators

- Arithmetic
```miranda
1 + 2
2 - 1
2 * 3
2 / 3
|| div expects two integer operands
365 div 7
|| mod expects two integer operands
365 mod 7
2 ^ 3
(1 / 3) * 3 || return fractional number as the first operand is fractional
1 ~= 1 || False, ~= is != in miranda
```

- abs
```miranda
abs (-33) || 33
```

- neg
```miranda
neg 33 || -33
abs (neg 33) || 33
```

- integer
```miranda
integer 3 || True
integer 3.0 || False
```

- entier

return the largest whole number that is less than the given fractional number
```miranda
entier 3.2 || 3
entier 3.7 || 3
entier (-3.2) || -4
entier (-3.7) || -4
```

- fractional number

Comparing two fractional numbers for equality is highly suspect due to decimal representation.
This can be resolved by using the `abs` function and by setting the `epsilon` value.
```miranda
abs(x - y) < 0.01
```

#### Characters (char)
No empty character can be defined
```miranda
`a` || 'a'
'' || syntax error
'1' + 1 || type error
```

##### Special Characters
```miranda
'\n' || newline

|| ASCII Code
'\065' || 'A'

|| char to num and num to char
code 'A' || 65
decode 65 || 'A'
```

#### String

concatenation ```++```
```miranda
"Hello" ++ " World" || "Hello World"
"" ++ "anything" || "anything"
```

subtraction ```--```
```miranda
"Hello me" -- " me" || Hlloe
"Hello me" -- "me" || Hllo e
"abc" -- "def" || abc
```

length ```#```
```miranda
# "Hello" || 5
# "\"Buy sth\"" || 9
```

indexing ```!```
```miranda
"Hey" ! 2 || 'y'
"abc" ! 999 || program error: subscript out of range
```

```show``` and ```shownum```
```miranda
"Hello" ++ (show 123) ++ "World" || "Hello123World"
"Hello" ++ (shownum 123) ++ "World" || "Hello123World"

(shownum (12 * 3)) ++ "world" || "36world"
```

#### Boolean

logical negation ```~```
```miranda
~True || False
~False || True
```

logical conjunction ```&```
```miranda
True & True || True
True & False || False
False & True || False
False & False || False
```

logical disjunction ```\/```
```miranda
True \/ True || True
True \/ False || True
False \/ True || True
False \/ False || False
```

example
```miranda
"Hello" ++ (show True) ++ "World" || "HelloTrueWorld"
'a' < 'b' || True
'A' < 'a' || True
```

#### Tuple

```miranda
date = (13, "March", 1066)
```
```miranda
date ~= (13, "March", 1066) || False
```
```miranda
((day, month, year), wine, price) = ((13, "May", 1966), "Margaux", 60)
```

## Functions

### Simple Functions
```miranda
twice x = x * 2
```

### Functions with more than one parameter
```miranda
|| To declare function with tuple as input
ismydate date = (date = (13, "March", 1066))
mydate = (13, "March", 1066)

ismydate mydate || True
ismydate (13, "March", 1066) || True

|| To declare the input types and output type
timestamp :: (num, [char]) -> [char] || if this line is removed, then show should be replpaced by shownum. otherwise type error due to polymorphic type
timestamp (time, message) = message ++ " at " ++ (show time) ++ "."
```

### Functions with more than one result
```miranda
divmod (x, y) = ((x div y), (x mod y))
```

### Functions without parameters
```miranda
mymessage () = "This is a message"
```

### Polymorphic Functions
```miranda
myfirst (x, y) = x
mysecond (x, y) = y
```

### Pattern Matching

Patterns may consist of constants (for example, integers but not fractional numbers, or the Boolean values True and False), 
tuples and formal parameter names.

Patterns containing arithmetic, relational or logical expressions are generally not allowed; the following are both wrong:

```miranda
|| illegae expression
wrong (x + y) = "silly"
also_wrong ("a" ++ anystring) = "starts with a"
```

However, it is legitimate to have patterns of the form (n + k), where n will evaluate
to a non-negative integer value and k is a non-negative integer constant. Hence the
following is legitimate, for all actual values of n greater than zero:
```miranda
|| speical case that is allowed
decrement (n + 1) = n
```

#### Alternative Patterns

All the alternative pattern must be the same type, including input and output type
```miranda
|| Must be bool -> bool
not True = False
not False = True
```

Duplicate
```miranda
both equal (x,x) = True
both equal (x,y) = False

both zero (0,0) = True
both zero (x,y) = False

step up (0,x) = x
step up (1,x) = x+1

plus (0,x) = x
plus (x,0) = x
plus (x,y) = x+y

twenty four hour (x,"a.m.") = x
twenty four hour (x,"p.m.") = x + 12
```

Order of evaluation: On exit from the editor Miranda will report syntax error, as the second case is unreachable.
```miranda
wrong or x = True
wrong or (False,False) = False
```

#### Guards (if)
```miranda
whichsign n = "Positive", if n > 0
            = "Zero", if n = 0
            = "Negative", otherwise
```

#### Alternative and Guarded Patterns
```miranda
check equiv ("zero",x) = "Equivalent", if x="Zero"
                       = "Not equivalent", otherwise
check equiv ("one",x) = "Equivalent", if x="One"
                      = "Not equivalent", otherwise
check equiv (n,x) = "Equivalent", if x=n
                  = "Out of range of this check", otherwise
```

### Type Information

#### Polymorphic type constraint

Same type version
```miranda
third same :: (*,*,*) -> *
third same (x,y,z) = z

third same (1,2,3) || 3
third same (1,2,"3") || type error
```
Any type version
```miranda
third any :: (*,**,***) -> ***
third any (x,y,z) = z

third any (1,2,3) || 3
third any (1,2,"3") || "3"
```

#### Type Synonyms
```miranda
dateformat == (num, [char], num)

sametype_triple * == (*,*,*)

triple * ** *** == (***,**,*)
```
Example of type synonym
```miranda
revNumTriple :: (sametype_triple num) -> (sametype_triple num)
revNumTriple (x,y,z) = (z,y,x)

revAnyTriple :: triple * ** *** -> triple *** ** *
revAnyTriple (x,y,z) = (z,y,x)
```

#### Algebraic Types

Algebraic types are defined with orders. 
i.e. colour ::= R | G | B, where R < G < B

### Recursive Functions
```miranda
plus :: (num,num) -> num
plus (x,0) = x
plus (x,y) = plus (x + 1, y - 1)

printdots :: num -> [char] 
printdots 0 = ""
printdots n = "." ++ (printdots (n - 1)), if n >= 1
            = error "printdots: negative input", otherwise
```

## List

Formal Definition: 
A list is either `empty` or `an element of a given type together with a list of elements of the same type`

empty list `[]`
```miranda
[] || empty list
```

### List Operations

```miranda
num_list = [1, 2, 3, 4, 5]
```

Extract the first item or the rest of the list
```miranda
hd num_list || 1
tl num_list || [2, 3, 4, 5]
```

List Construction
```miranda
(:) ::
|| * -> [*] -> [*]
```

Add an element to list
```miranda
list1 = "a" : []

"new" : list1 || ["new", "a"]
```

Append list to list
```miranda
list2 = "abc" : "def" : []
list3 = "xy" : "z" : []

list2 ++ list3 || ["bc", "xy", "z"]
```

List Subtraction
```miranda
['c', 'b', 'c', 'a', 't', 's'] -- ['c', 's'] || ['b', 'c', 'a', 't']

['c', 'c', 'a', 't', 's'] -- ['c'] || ['c', 'a', 't', 's']
```

List Length
```miranda
# [345, 234, 567] || 3
```

List Indexing
```miranda
["ben", "james", "billy"] ! 2 || "billy"
```

### List Comprehension

Gererate all permutations of a list
```miranda
permutations [] = [[]]
permutations anylist
= [ front : rest | front <- anylist;
rest <- permutations(anylist--[front]) ]
```

Generate cartesian product
```miranda
cartesian_product :: [*] -> [**] -> [(*, **)]
cartesian_product list_a list_b = [(a, b) | a <- list_a; b <- list_b]
```

Generate list with conditions
```miranda
list_condition :: num -> [num]
list_condition n = [a | a <- [1..n]; n mod a = 0]
```

test_triangle n = [(a, b, c) // a, b, c <- [1..n]; a^2 + b^2 = c^2]

### Dotdot Notation

This abbreviated form may only be used for ascending lists.
if a descending list is specified, the system returns the empty list.
```miranda
[1..4] || [1, 2, 3, 4]

[4..1] || []

[-2..2] || [-2, -1, 0, 1, 2]

[2..-2] || []

[-2, 0..10] || [-2. 0, 2, 4, 6, 8, 10]

[1, 3..10] || [1, 3, 5, 7, 9]

[3, 1..-5] || [3, 1, -1, -3, -5]
[3, 1..-8] || [3, 1, -1, -3, -5, -7]
```


## Error

- syntax error
- type error
- program error

```miranda
'' || syntax error
|| Since Miranda believe - is the argument for abs, it returns type error
abs -33 || type error
|| div expects two integer operands
365 div 7.0 || program error
```

## Good to Know
Comment
```miranda
|| This is a comment
```

Literate Script

Used when lines of comments are more than coding
```miranda
>|| literate script version of above program

Program "spendingmoney.m".
Calculates the amount ofholiday spending money.
Only deals with three different currencies.

>amountofsterling = 200.0 || amount ofmoney available 

different exchange rates

>uktous =1.70
>uktodm =2.93
>uktofr =10.94

amount ofspending money in different currencies
>usspendingmoney = amountofsterling * uktous
>dmspendingmoney = amountofsterling * uktodm
>frspendingmoney = amountofsterling * uktofr
```

Function as Value
```miranda
tw = twice
tw 3 || 6
```

## Special Example
```miranda
(2 < 3 < 4) || True

((2 < 3) < 4) || error

abs twice 3 || interpreted as (abs twice) 3, hence type error
abs (twice 3) || 6
```

To-Do

Exercise in Miranda book p62
convert an integer to a string
