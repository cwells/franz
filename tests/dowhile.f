#
# do/while loop
#

print("Testing do/while loop...")
errors = 0

a = 10
result = do {
    a -= 1
} while a > 1

try assert result == 1 rescue errors += 1

print(if errors "Some tests failed ({errors}) errors\n" else "passed!\n")
