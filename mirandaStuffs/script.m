||This is a comment

hours = 24

message = "Hello World"

days = ((4 * 30) + (7 * 31) + 28)

date = (13, "March", 1066)

((day, month, year), wine, price) = ((13, "May", 1966), "Margaux", 60)

twice x = x * 2

tw = twice

ismydate date = (date = (13, "March", 1066))

timestamp :: (num, [char]) -> [char]
timestamp (time, message) = message ++ " at " ++ (show time) ++ "."

divmod (x, y) = ((x div y), (x mod y))

mymessage () = "This is a message"

myfirst (x, y) = x
mysecond (x, y) = y

dup x = (x, x)

not True = False
not False = True

whichsign n = "Positive", if n > 0
            = "Zero", if n = 0
            = "Negative", otherwise

            check_equiv ("zero",x) = "Equivalent", if x="Zero"
            = "Not equivalent", otherwise
check_equiv ("one",x) = "Equivalent", if x="One"
           = "Not equivalent", otherwise
check_equiv (n,x) = "Equivalent", if x=n
       = "Out of range of this check", otherwise

dateformat == (num, [char], num)

sametype_triple * == (*,*,*)
revNumTriple :: (sametype_triple num) ->  (sametype_triple num)
revNumTriple (x,y,z) = (z,y,x)

triple * ** *** == (***,**,*)
revAnyTriple :: triple * ** *** -> triple *** ** *
revAnyTriple (x,y,z) = (z,y,x)

plus :: (num, num) -> num
plus (x,0) = x
plus (x,y) = plus (x + 1, y - 1)


printdots :: num -> [char]
printdots 0 = ""
printdots n = "." ++ (printdots (n - 1)), if n >= 1
 = error "printdots: negative input", otherwise

num_list = [1, 2, 3, 4, 5]

list1 = "a" : []
list2 = "abc" : "def" : []
list3 = "xy" : "z" : []

threes :: [num] -> num
threes [] = 0
threes (front : rest) = 1 + threes rest, if front = 3
threes (front : rest) = 0 + threes rest, otherwise

f x y = x + y
pf y = f 3 y

startswith :: ([*], [*]) -> bool
startswith ([], y) = True
startswith (x, []) = False
startswith ((x:xs),(y:ys)) = (x=y) & startswith(xs,ys)

test_tuple (x, y, z) = (z, y, x)

|| challenges of counting 1 and 2
f_count :: (num, num, num, num) -> [num] -> (num, num, num)
f_count (a, b, c, d) (x:xs)
  = f_count (a+1, b, c+1, d) xs, if x = 1
  = f_count (a, b+1, 0, max[c, d]) xs, if x = 2
  = (a, b, max[c, d]), if x = 0

|| the main function should be put at the top in miranda
count_one_two :: [num] -> (num, num, num)
count_one_two = f_count (0, 0, 0, 0)

mylist * ::= Empty | Element * (mylist *)

numchar ::= Character char | Number num

numchartree ::= Emptytree | Node numchar (numchartree) (numchartree)

insertnum :: numchartree -> num -> numchartree
insertnum Emptytree x = Node (Number x) Emptytree Emptytree
|| insertnum wholetree x = createtree(decompose(wholeTree))
|| where flatterntree Nodei
|| first flattern the tree then build up new tree

