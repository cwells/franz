#
# test math operators and order of operations
#

print("Testing math operators and order of operations...")
errors = 0

try assert 1 + 2 * 3 == 7 rescue errors += 1
try assert (1 + 2) * 3 == 9 rescue errors += 1
try assert (1 - 2) * 3 == -3 rescue errors += 1
try assert 1 - 2 * 3 == -5 rescue errors += 1
try assert (3 * 3) ^ 2 == 81 rescue errors += 1
try assert 3 * 3 ^ 2 == 27 rescue errors += 1
try assert 4 * (3 + 3) == 24 rescue errors += 1
try assert 4 / 2 + 6 == 8 rescue errors += 1
try assert 4 / (2 + 6) == 0.5 rescue errors += 1
try assert 60 % 21 // 2 == 9 rescue errors += 1
try assert 63 % (21 // 2) == 3 rescue errors += 1

a = 8
assert (a += 1) == 9
assert (a -= 1) == 8
assert (a /= 2) == 4.0
assert (a //= 2) == 2
assert (a %= 2) == 0

print(if errors "Some tests failed ({errors}) errors\n" else "passed!\n")
