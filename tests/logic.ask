#
# test logical operators
#

print("Testing logical operators...")
errors = 0

try assert true and true rescue errors += 1
try assert true and false rescue nil else errors += 1
try assert false and true rescue nil else errors += 1
try assert false and false rescue nil else errors += 1

try assert true or true rescue errors += 1
try assert true or false rescue errors += 1
try assert false or true rescue errors += 1
try assert false or false rescue nil else errors += 1

print(if errors "Some tests failed ({errors}) errors\n" else "passed!\n")
