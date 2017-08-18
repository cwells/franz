#
# test yield
#

print("Testing yield...")
errors = 0

loop = fn (n: int)
    for i in 1 to n
        yield i

pairs = fn (n: int)
    for i in 1 to n {
        # print ("pairs i:{i}\n")
        yield (yield i) ^ 2
    }

squares = fn (n: int)
    for i in 1 to n
        yield [ i, i ^ 2 ]

try assert [ loop(5) ] == [ 1, 2, 3, 4, 5 ] rescue errors += 1
assert [ pairs(4) ] == [1, 1, 2, 4, 3, 9, 4, 16]
try assert [ squares(4) ] == [ [1, 1], [2, 4], [3, 9], [4, 16] ] rescue errors += 1

# test infinite generator
integers = fn () {
    i = 0
    while true
        yield i += 1
}

scan = fn (n: int) {
    retval = []
    for i in integers() {
        retval += [ i ]
        if i >= n return retval
    }
}

try assert scan(100) == 1 to 100 rescue errors += 1

print(if errors "Some tests failed ({errors}) errors\n" else "passed!\n")
