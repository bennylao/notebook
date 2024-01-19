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

#### Alternative Patterns

All the alternative pattern must be the same type, including input and output type
```miranda
|| Must be bool -> bool
not True = False
not False = True
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
