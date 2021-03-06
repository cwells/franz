#
# test return <value>
#

print("Testing return...")
errors = 0

f = fn () # return <value>
    for i in 1 to 5
        if i == 5 return "string"

g = fn (n: int) # return <complex expression>, nested return
    return for i in 1 to n {
        f = fn () return n * i
        f()
    }

try assert f() == "string" rescue errors += 1
try assert g(20) == 400 rescue errors += 1

print(if errors "Some tests failed ({errors}) errors\n" else "passed!\n")
