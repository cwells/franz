import time
import getpass

from prompt_toolkit import prompt, AbortAction
from prompt_toolkit.contrib.completers import WordCompleter
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.styles import style_from_dict
from prompt_toolkit.token import Token
from prompt_toolkit.layout.lexers import PygmentsLexer

from pygments.style import Style
from pygments.token import Token
from pygments.styles.default import DefaultStyle

from lark.common import UnexpectedToken
from lark.lexer import UnexpectedInput

from .pygments import FranzLexer

class ReplStyle(Style):
    styles = {
        Token.Menu.Completions.Completion.Current: 'bg:#00aaaa #000000',
        Token.Menu.Completions.Completion: 'bg:#008888 #ffffff',
        Token.Menu.Completions.ProgressButton: 'bg:#003333',
        Token.Menu.Completions.ProgressBar: 'bg:#00aaaa',

        Token.Toolbar: '#ffffff bg:#333333',
    }
    styles.update(DefaultStyle.styles)

def __repl(parser, interpreter):
    history = InMemoryHistory()
    toolbar_value = 'Hello, %s. Press [Alt]+[Enter] to evaluate an expression.' % getpass.getuser()

    while True:
        name_completer = WordCompleter(sorted(interpreter.context))

        code = prompt('> ',
            multiline     = True,
            completer     = name_completer,
            history       = history,
            style         = ReplStyle,
            mouse_support = True,
            lexer         = PygmentsLexer(FranzLexer),
            auto_suggest  = AutoSuggestFromHistory(),
            get_bottom_toolbar_tokens = lambda cli: [(Token.Toolbar, toolbar_value)],
            on_abort      = AbortAction.RETRY
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
            toolbar_value = "Error: %s" % e.args
            continue
        else:
            toolbar_value = "time: {:0.4f} value: {}".format(time.time() - start_eval_time, retval)


def repl(parser, interpreter):
    print("Franz v0.0\n")
    while True:
        try:
            __repl(parser, interpreter)
        except KeyboardInterrupt:
            continue
