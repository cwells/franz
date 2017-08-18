#
# test pipes
#

#
# BUG: https://github.com/cwells/franz/issues/1
#
# These tests coerce the generator argument to
# a list in order to bypass bug #1, but this isn't
# currently working as intended.
#

print("Test pipes...")
errors = 0

a = fn (n: int)
    for i in 1 to n
        yield i

b = fn (iter: list)
    for i in iter
        yield i ^ 2

c = fn (iter: list)
    for i in iter
        yield i ^ 2

pipes = [ a(4) -> b -> c ]
nested = [ c(b(a(4))) ]
known = [ 1, 16, 81, 256 ]

try assert pipes == nested rescue errors += 1
try assert pipes == known rescue errors += 1

print(if errors "Some tests failed ({errors}) errors\n" else "Passed with caveat: see source code of this test.\n")
