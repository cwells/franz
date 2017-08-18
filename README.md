> _K. does not know whether this is some sort of joke or not._ ~ Franz Kafka, _The Trial_

# Franz
<img align="right" width="100" height="100" src="https://github.com/cwells/franz/blob/master/franz.png">

Franz is a toy interpreter I've implemented using Python and [Lark](https://github.com/erezsh/lark). It's completely
expression-oriented; everything except for operators is an expression that evaluates to a sensible value. 

It's not fast, there are [serious bugs](https://github.com/cwells/franz/issues/1), and it's not done. [Even the basic 
syntax is highly subject to change](https://github.com/cwells/franz/issues/2). It lacks major features 
such as object support.

It's also my first attempt at language design, with the goal of trying to implement a particular set of features 
I'd like to see in real languages. This exercise is about language design, not language performance.

One thing to note is that Franz is whitespace-sensitive in that you must have whitespace around tokens.
e.g. `a - 1` is subtraction, whereas `a-1` is a variable or function named "a-1". This restriction allows
you to use characters such as `-` or `?` as part of a variable or function name.

`./franz` will accept a filename containing Franz source on the command line or 
start a simple REPL if no file is provided.

Here's a recursive implementation of a Fibonacci sequence. This is an elegant, but inefficient algorithm. 
Calculating 25 numbers takes 13.28s on my computer. 

```
$ ./franz 
Franz v0.0 (\h for help)
>>> fibonacci-sequence = fn (start: int, end: int) {
...     fibonacci-number = fn (nth: int)
...         if nth <= 1
...             nth
...         else
...             fibonacci-number(nth - 1) + fibonacci-number(nth - 2)
... 
...     for i in start to end
...         yield fibonacci-number(i)
... }
<__main__.Function object at 0x7f514a14dfd0>
>>> sequence = [ fibonacci-sequence(start: 1, end: 20) ]
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
>>> 
```

Faster Fibonacci generator. Calculating 25 numbers takes 0.001s on my computer. 10,000 numbers takes only 1.24s.
```
$ ./franz 
Franz v0.0 (\h for help)
>>> fibonacci-sequence = fn (n: int) {
...     a = b = 1
...     for i in 3 to n + 2
...         (a, b) = (b, (yield a) + b)
... }
<__main__.Function object at 0x7f07d9cbc160>
>>> 
>>> sequence = [ fibonacci-sequence(20) ]
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
>>> 
```

Of interest in the second example is the fact that `yield a` is an expression that evaluates to `a`, 
so it can be used in subsequent expressions.


See the [tests/](https://github.com/cwells/franz/tree/master/tests) directory for more examples.
