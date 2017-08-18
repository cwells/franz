#
# test arrays and subscripts
#

print("Testing arrays and subscripts...")
errors = 0

a = []
try assert a == [] rescue errors += 1

a = [ 1, 2, 3 ]
try assert a == [ 1, 2, 3 ] rescue errors += 1

a = [ 1 to 5 ]
try assert a == [ 1, 2, 3, 4, 5 ] rescue errors += 1

a = [ 5 to 1 step -1 ]
assert a == [ 5, 4, 3, 2, 1 ]

a = [ 1 to 10 step 2 ]
try assert a == [ 1, 3, 5, 7, 9 ] rescue errors += 1
try assert a[0] == 1 rescue errors += 1
try assert a[-1] == 9 rescue errors += 1
try assert a[1] * a[2] == 15 rescue errors += 1

try assert [ 1, 2, 3, 4 ][2] == 3 rescue errors += 1

x = a[1 - 1] # a[0]
y = a[2 - 1] # a[1]
try assert x + y == 4 rescue errors += 1

f = fn (n: int)
    return [ n to 1 step -1 ]

try assert f(5)[2] == 3 rescue errors += 1

a = [ 1 to 10 ]
try assert a[ 2:4 ] == [ 3, 4 ] rescue errors += 1
try assert a[ 0: ] == [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] rescue errors += 1
try assert a[ :-1 ] == [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ] rescue errors += 1
try assert a[ : ] == a rescue errors += 1

print(if errors "Some tests failed ({errors}) errors\n" else "passed!\n")
