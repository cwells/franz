import readline
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
    "\T to show AST",
    "\q (or ctrl+d) to quit"
]

def help():
    for c in COMMANDS:
        print("%s" % c)


def repl(parser, interpreter):
    # naive repl
    print("Franz v0.0 (\h for help)")
    readline.set_completer( lambda text, state: [
        c for c in sorted(interpreter.context) if c.startswith(text)
    ][state])
    readline.parse_and_bind("tab: complete")
    code_block = []
    last = ''
    prompt = '>>> '
    while True:
        try:
            s = input(prompt)
        except EOFError:
            break
        if not s:
            continue

        if s == '\c':
            code_block = []
            prompt = '>>> '
            continue
        elif s == '\h':
            help()
            continue
        elif s == '\l':
            print(last)
            continue
        elif s == '\q':
            raise SystemExit
        elif s == '\s':
            print('\n'.join(code_block))
            continue
        elif s == '\T':
            try:
                print(ast.pretty())
            except UnboundLocalError:
                print("\n")
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

