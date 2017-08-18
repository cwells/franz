#
# test assignment
#

print("Testing assignment...")
errors = 0

(a, b) = (1, 2)
try assert a == 1 and b == 2 rescue errors += 1

a = b = 9
try assert a == 9 and b == 9 rescue errors += 1

a = 8
try assert (a += 1) == 9 rescue errors += 1
try assert (a -= 1) == 8  rescue errors += 1
try assert (a /= 2) == 4.0 rescue errors += 1
try assert (a *= 2) == 8.0 rescue errors += 1
try assert (a //= 2) == 4 rescue errors += 1
try assert (a %= 2) == 0 rescue errors += 1

try assert (a ?= b) == b rescue errors += 1
# try assert (a ?= c) == a rescue errors += 1           # c is undef
# try assert (a ?= c or b) == b rescue errors += 1      # c is undef
# try assert (a ?= c or b or a) == b rescue errors += 1 # c is undef

try assert ((i, j) = (1, 2)) == [ 1, 2 ] rescue errors += 1
try assert i == 1 and j == 2 rescue errors += 1
try assert ((i, j) ?= (3, 4, 5)) == [ 5 ] rescue errors += 1
try assert i == 3 and j == 4 rescue errors += 1
try assert ((i, j, k) ?= (3, 4)) == [ ] rescue errors += 1
try assert i == 3 and j == 4 and k == nil rescue errors += 1

# (a, b) = (1, 2)
# try assert ((i, j) ?= (a, b, c)) == [ ] rescue errors += 1 # c is undef
# try assert i == 1 and j == 2 rescue errors += 1

# n at a time
triplets = fn (items: list) do {
    items = ((a, b, c) ?= items)
    yield [ a, b, c ]
} while items

try assert [ triplets(1 to 9) ] == [
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]
rescue errors += 1

print(if errors "Some tests failed ({errors}) errors\n" else "passed!\n")
