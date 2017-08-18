a = fn (n: int)
    for i in 1 to n
        yield i

b = fn (iter: list)
    for i in iter
        yield i ^ 2

c = fn (iter: list)
    for i in iter
        yield i ^ 2

value = [ a(4) -> b -> c ]
print("value: {value}\n")

value = [ c(b(a(4))) ]
print("value: {value}\n")

assert value == [ 1, 16, 81, 256 ]

# assert value == c(b(a(10)))