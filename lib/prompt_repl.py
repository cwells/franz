import time

from prompt_toolkit import prompt

from lark.common import UnexpectedToken
from lark.lexer import UnexpectedInput

COMMANDS = [
    "\c to clear buffer",
    "\s to show buffer",
    "\l to show last successful expression",
    "\\t <expr> to time execution of <expr>",
    "\T to show AST",
    "\q (or ctrl+d) to quit"
]

def help():
    for c in COMMANDS:
        print("%s" % c)

def __repl(parser, interpreter):
    code_block = []
    last = ''

    while True:
        start_eval_time = None

        s = prompt('> ', multiline=True)

        if not s.strip():
            continue

        if s == '\c':
            code_block = []
            continue
        elif s in ('\h', '\?'):
            help()
            continue
        elif s == '\l':
            print(last, "\n")
            continue
        elif s == '\q':
            print("Exiting.\n")
            raise SystemExit
        elif s == '\s':
            print('\n'.join(code_block))
            continue
        elif s.startswith('\\t'):
            start_eval_time = time.time()
            s = s[2:]
        elif s == '\T':
            try:
                print(ast.pretty())
            except UnboundLocalError:
                pass
            continue

        code_block.append(s)
        s = '\n'.join(code_block)

        try:
            ast = parser.parse(s)
        except UnexpectedToken:
            continue
        except UnexpectedInput:
            code_block = code_block[:-1]
            continue

        code_block = []

        try:
            retval = interpreter.eval(ast)
        except Exception as e:
            print("Error:", *e.args, "\n")
            continue
        else:
            if retval: print(repr(retval))
            last = s
            if start_eval_time is not None:
                print("Runtime:", time.time() - start_eval_time)

def repl(parser, interpreter):
    print("Franz v0.0 (\h for help)")
    # readline.set_completer(lambda text, state: [
    #    c for c in sorted(interpreter.context) if c.startswith(text)
    #][state])
    # readline.parse_and_bind("tab: complete")

    while True:
        try:
            __repl(parser, interpreter)
        except KeyboardInterrupt:
            continue
