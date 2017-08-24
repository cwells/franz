import os
import time
from pprint import pprint
from pathlib import Path

from prompt_toolkit import prompt, AbortAction
from prompt_toolkit.contrib.completers import WordCompleter
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.styles import style_from_pygments
from prompt_toolkit.token import Token
from prompt_toolkit.layout.lexers import PygmentsLexer

from lark.common import UnexpectedToken
from lark.lexer import UnexpectedInput

from .pygments import FranzLexer, repl_styles


def prepare_style(style):
    style.styles.update({
        # menu
        Token.Menu.Completions.Completion.Current: 'bg:#00aaaa #000000',
        Token.Menu.Completions.Completion: 'bg:#008888 #ffffff',
        Token.Menu.Completions.ProgressButton: 'bg:#003333',
        Token.Menu.Completions.ProgressBar: 'bg:#00aaaa',
        # toolbar
        Token.Toolbar: '#ffffff bg:#333333',
        # prompt
        Token.Prompt:       '#444444',
        Token.Continuation: '#333333',
    })
    return style_from_pygments(style)

def get_prompt_tokens(cli):
    return [ (Token.Prompt, '>>> ') ]

def get_continuation_tokens(cli, width):
    return [(Token.Continuation, '.' * (width - 1))]

def repl(parser, interpreter, style_name='default'):
    print("Franz v0.0\n")
    history_file = os.path.join(str(Path.home()), '.franz-history')
    history = FileHistory(history_file)
    toolbar_value = 'Press [Alt+Enter] to evaluate an expression. [Ctrl+d] to exit. History saved in %s.' % history_file
    style = prepare_style(repl_styles[style_name])

    while True:
        name_completer = WordCompleter(sorted(interpreter.context))

        code = prompt(
            multiline     = True,
            completer     = name_completer,
            history       = history,
            style         = style,
            mouse_support = False,
            lexer         = PygmentsLexer(FranzLexer),
            auto_suggest  = AutoSuggestFromHistory(),
            on_abort      = AbortAction.RETRY,
            patch_stdout  = True,
            true_color    = True,
            get_bottom_toolbar_tokens = lambda cli: [(Token.Toolbar, toolbar_value)],
            get_prompt_tokens         = get_prompt_tokens,
            get_continuation_tokens   = get_continuation_tokens,
        )

        if not code.strip(): continue
        if code == '\\var':
            pprint(interpreter.context)
            continue

        try:
            ast = parser.parse(code)
        except (UnexpectedToken, UnexpectedInput) as e:
            toolbar_value = str(e)
            continue

        try:
            start_eval_time = time.time()
            retval = interpreter.eval(ast)
        except Exception as e:
            toolbar_value = "Error: %s" % e.args
            continue
        else:
            toolbar_value = "Time: {:0.4f}, Value: {}".format(time.time() - start_eval_time, str(retval))


