import time

from prompt_toolkit import prompt
from prompt_toolkit.contrib.completers import WordCompleter
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.styles import style_from_dict
from prompt_toolkit.token import Token

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


style = style_from_dict({
    Token.Toolbar: '#ffffff bg:#333333',
})

def __repl(parser, interpreter):
    code_block = []
    last = ''
    toolbar_value = ''
    history = InMemoryHistory()

    while True:
        name_completer = WordCompleter(sorted(interpreter.context))
        start_eval_time = None

        s = prompt('> ',
            multiline    = True,
            completer    = name_completer,
            history      = history,
            style        = style,
            auto_suggest = AutoSuggestFromHistory(),
            get_bottom_toolbar_tokens = lambda cli: [(Token.Toolbar, toolbar_value)]
        )

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
            start_eval_time = time.time()
            retval = interpreter.eval(ast)
        except Exception as e:
            print("Error:", *e.args, "\n")
            continue
        else:
            toolbar_value = "time: {:0.4f} value: {}".format(time.time() - start_eval_time, retval)
            last = s


def repl(parser, interpreter):
    print("Franz v0.0 (\h for help)\nPress [Alt]+[Enter] to complete an expression.")
    while True:
        try:
            __repl(parser, interpreter)
        except KeyboardInterrupt:
            continue
