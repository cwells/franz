g = fn (b: int) {
    for i in 1 to b
        yield i
}

val = g(10)
print("{val}\n")

f = fn (a: int) {
    g = fn (b: int) {
        for i in 1 to b
            yield i
    }

    for i in g(a)
        yield i
}

val = f(5)
print("{val}\n")