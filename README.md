# franz
Simple expression-oriented language written in Python

Franz is a toy interpreter I've written using Python and [Lark](https://github.com/erezsh/lark).

It's not fast, there are bugs, and it's not done. 

It's also my first attempt at language design, and this 
language will try to implement a particular set of features 
I'd like to see in real languages.

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

