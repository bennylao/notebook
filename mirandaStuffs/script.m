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
