#!/usr/bin/env python
from __future__ import unicode_literals

import time

from lark.common import UnexpectedToken
from lark.lexer import UnexpectedInput

from prompt_toolkit.application import Application
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.enums import DEFAULT_BUFFER
from prompt_toolkit.interface import CommandLineInterface
from prompt_toolkit.key_binding.defaults import load_key_bindings
from prompt_toolkit.keys import Keys
from prompt_toolkit.layout.containers import VSplit, HSplit, Window
from prompt_toolkit.layout.controls import BufferControl, FillControl, TokenListControl
from prompt_toolkit.layout.dimension import LayoutDimension as D
from prompt_toolkit.shortcuts import create_eventloop
from prompt_toolkit.token import Token
from prompt_toolkit.layout.lexers import PygmentsLexer
from prompt_toolkit.styles.from_pygments import style_from_pygments

from pygments.styles import get_style_by_name

from .pygments import FranzLexer


layout = HSplit([
    Window(content=BufferControl(buffer_name=DEFAULT_BUFFER, lexer=PygmentsLexer(FranzLexer))),
    Window(height=D.exact(1), content=FillControl(u"\u2015", token=Token.Line)),
    Window(content=BufferControl(buffer_name='RESULT')),
])

def get_titlebar_tokens(cli):
    return [
        (Token.Title, ' Franz 0.0 '),
        (Token.Title, ' (Press [Meta-Enter] to evaluate buffer. Press [Ctrl-Q] to quit.) '),
    ]

layout = HSplit([
    Window(height=D.exact(1), content=TokenListControl(get_titlebar_tokens, align_center=True)),
    Window(height=D.exact(1), content=FillControl(u"\u2015", token=Token.Line)),
    layout,
])

registry = load_key_bindings()

@registry.add_binding(Keys.ControlC, eager=True)
@registry.add_binding(Keys.ControlQ, eager=True)
def _(event):
    event.cli.set_return_value(None)

buffers = {
    DEFAULT_BUFFER: Buffer(is_multiline=True),
    'RESULT': Buffer(is_multiline=True),
}

def repl(parser, interpreter, style_name='default'):
    @registry.add_binding(Keys.Escape, Keys.Enter) # meta-enter/alt-enter
    def _(event):
        code = buffers[DEFAULT_BUFFER].text
        try:
            ast = parser.parse(code)
        except (UnexpectedToken, UnexpectedInput) as e:
            toolbar_value = str(e)
            return

        try:
            start_eval_time = time.time()
            retval = interpreter.eval(ast)
        except Exception as e:
            toolbar_value = "Error: %s" % e.args
            return
        else:
            buffers['RESULT'].text = str(retval)
            toolbar_value = "Time: {:0.4f}, Value: {}".format(time.time() - start_eval_time, str(retval))

    style = style_from_pygments(get_style_by_name(style_name))

    application = Application(
        layout        = layout,
        buffers       = buffers,
        mouse_support = True,
        style         = style,
        use_alternate_screen = True,
        key_bindings_registry = registry
    )

    eventloop = create_eventloop()

    try:
        cli = CommandLineInterface(application=application, eventloop=eventloop)
        cli.run()

    finally:
        eventloop.close()

