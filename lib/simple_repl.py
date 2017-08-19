import readline
import time
from lark.common import UnexpectedToken
from lark.lexer import UnexpectedInput

readline.parse_and_bind('tab: complete')
readline.parse_and_bind('set editing-mode emacs')

try: input = raw_input
except NameError: pass

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
    # naive repl
    code_block = []
    last = ''
    prompt = '>>> '

    while True:
        start_eval_time = None

        try:
            s = input(prompt)
        except EOFError:
            print("Exiting.\n")
            raise SystemExit

        if not s:
            continue

        if s == '\c':
            code_block = []
            prompt = '>>> '
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
            prompt = '... '
            continue
        except UnexpectedInput:
            prompt = '... '
            code_block = code_block[:-1]
            continue

        code_block = []
        prompt = '>>> '

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
    readline.set_completer(lambda text, state: [
        c for c in sorted(interpreter.context) if c.startswith(text)
    ][state])
    readline.parse_and_bind("tab: complete")

    while True:
        try:
            __repl(parser, interpreter)
        except KeyboardInterrupt:
            continue
