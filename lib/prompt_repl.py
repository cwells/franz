import time
import getpass

from prompt_toolkit import prompt
from prompt_toolkit.contrib.completers import WordCompleter
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.styles import style_from_dict
from prompt_toolkit.token import Token

from lark.common import UnexpectedToken
from lark.lexer import UnexpectedInput


def __repl(parser, interpreter):
    history = InMemoryHistory()
    toolbar_value = 'Hello, %s.' % getpass.getuser()

    style = style_from_dict({
        Token.Toolbar: '#ffffff bg:#333333',
    })

    while True:
        name_completer = WordCompleter(sorted(interpreter.context))

        code = prompt('> ',
            multiline    = True,
            completer    = name_completer,
            history      = history,
            style        = style,
            auto_suggest = AutoSuggestFromHistory(),
            get_bottom_toolbar_tokens = lambda cli: [(Token.Toolbar, toolbar_value)]
        )

        if not code.strip(): continue

        try:
            ast = parser.parse(code)
        except (UnexpectedToken, UnexpectedInput):
            continue

        try:
            start_eval_time = time.time()
            retval = interpreter.eval(ast)
        except Exception as e:
            print("Error:", *e.args, "\n")
            continue
        else:
            toolbar_value = "time: {:0.4f} value: {}".format(time.time() - start_eval_time, retval)


def repl(parser, interpreter):
    print("Franz v0.0 Press [Alt]+[Enter] to evaluate an expression.")
    while True:
        try:
            __repl(parser, interpreter)
        except KeyboardInterrupt:
            continue
