#
# f argument passing
#

print("Testing function arguments...")
errors = 0

f = fn (a: int, b: int, c: int, d: int)
    v = a + b + c + d

g = fn () # empty argument list
    return nil

a = 1
b = 2
try assert f(a: 1, b: 2, c: 3, d: 4) == 10 rescue errors += 1
try assert f(1, 2, 3, 4) == 10 rescue errors += 1
try assert f(1, 2, c: 3, d: 4) == 10 rescue errors += 1
try assert f(a, b, b + 1, d: b * 2) == 10 rescue errors += 1 # BUG: parse error at +

try assert f( # complex expression
    a: 1,
    b: 2,
    c: 3,
    d: for i in 1 to 4 i
) == 10
rescue errors += 1

try assert f( # complex expression
    a: 1,
    b: 2,
    c: 3,
    d: if a == 1 for i in 1 to 4 i
) == 10
rescue errors += 1

try assert g() == nil rescue errors += 1
try assert g(1) == nil rescue nil else errors += 1

print(if errors "Some tests failed ({errors}) errors\n" else "passed!\n")

