#
# this is actually the worst way to compute a fibonacci sequence
# but I chose it because it tests recursion and nested scopes
#

print("Testing fibonacci sequence (recursion, scope)...")
errors = 0

fibonacci-sequence = fn (start: int, end: int) {
    fibonacci-number = fn (nth: int)
        if nth <= 1
            nth
        else
            fibonacci-number(nth - 1) + fibonacci-number(nth - 2)

    for i in start to end
        yield fibonacci-number(i)
}

sequence = [ fibonacci-sequence(start: 1, end: 20) ]

try assert sequence == [
    1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,
    233, 377, 610, 987, 1597, 2584, 4181, 6765
]
rescue errors += 1

#
# faster, non-recursive function
#
fibonacci-sequence = fn (n: int) {
    a = b = 1
    for i in 3 to n + 2
        (a, b) = (b, (yield a) + b)
}

sequence = [ fibonacci-sequence(20) ]

try assert sequence == [
    1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,
    233, 377, 610, 987, 1597, 2584, 4181, 6765
]
rescue errors += 1

print(if errors "Some tests failed ({errors}) errors\n" else "passed!\n")

