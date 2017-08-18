> "K. does not know whether this is some sort of joke or not." ~ Franz Kafka, The Trial

# franz
Simple expression-oriented language written in Python

Franz is a toy interpreter I've written using Python and [Lark](https://github.com/erezsh/lark).

It's not fast, there are bugs, and it's not done. 

It's also my first attempt at language design, and this 
language will try to implement a particular set of features 
I'd like to see in real languages.

One thing to note is that Franz is whitespace-sensitive in that you must have whitespace around tokens.
e.g. `a - 1` is subtraction, `a-1` is a variable or function named "a-1".

Franz will accept a filename containing Franz source on the command line or 
start a simple REPL if no file is provided.

```
#
# inefficient algorithm intentionally chosen
#
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
```

