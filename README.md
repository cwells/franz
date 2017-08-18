> _K. does not know whether this is some sort of joke or not._ ~ Franz Kafka, _The Trial_

# franz
<img align="right" width="100" height="100" src="https://github.com/cwells/franz/blob/master/franz.png">

Franz is a toy interpreter I've implemented using Python and [Lark](https://github.com/erezsh/lark). It's completely
expression-oriented. Everything except for operators is an expression that evaluates to a sensible value. 

It's not fast, there are [serious bugs](https://github.com/cwells/franz/issues/1), and it's not done. [Even the basic 
syntax is highly subject to change](https://github.com/cwells/franz/issues/2). It lacks major features 
such as object support.

It's also my first attempt at language design, and this 
language will try to implement a particular set of features 
I'd like to see in real languages. This exercise is about language design, not language performance.

One thing to note is that Franz is whitespace-sensitive in that you must have whitespace around tokens.
e.g. `a - 1` is subtraction, whereas `a-1` is a variable or function named "a-1". This restriction allows
you to use characters such as `-` or `?` as part of a variable or function name.

`./franz` will accept a filename containing Franz source on the command line or 
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

See the [tests/](https://github.com/cwells/franz/tree/master/tests) directory for more examples.
