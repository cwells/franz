import importlib

from pygments.lexer import RegexLexer, bygroups
from pygments.styles import STYLE_MAP
from pygments.token import *


def load_style(full_class_string):
    modulename, styleclass = full_class_string.split('::')
    module = importlib.import_module("pygments.styles." + modulename)
    return getattr(module, styleclass)


repl_styles = {}
for name, import_info in STYLE_MAP.items():
    repl_styles[name] = load_style(import_info)
    repl_styles[name].styles[Whitespace] = '' # some styles underline ws


class FranzLexer(RegexLexer):
    name = 'Franz Lexer'
    tokens = {
        'root': [
            (r'"', String.Double, 'double-quote'),
            (r'[0-9]+(\.[0-9]+)?', Number),
            (r'\b(if|else|for|while|in|to|fn|ⲗ|try|rescue|assert|include|yield|return|break|continue)\b', Keyword.Reserved),
            (r'\b(int|str|any|float|list|dict|bool)\b', Keyword.Type),
            (r'\b(and|or|not)\b', Operator.Word),
            (r'#.*?$', Comment.Single),
            (r'([a-zA-Z][a-zA-Z0-9_!?\-%$]*)(\s*)(=)(\s*)(fn)',
                bygroups(Name.Function.Definition, Whitespace, Operator, Whitespace, Keyword.Reserved)),
            (r'\b([a-zA-Z][a-zA-Z0-9_!?\-%$]*)(\s*)([(])', bygroups(Name.Function, Whitespace, Punctuation)),
            (r'\b[a-zA-Z][a-zA-Z0-9_!?\-%$]*\b', Name),
            (r'\s+([*+\-^=<>%/?]+)\s+', Operator),
            (r'[@().,:;\[\]]', Punctuation),
            (r'[{}]', Punctuation.Braces),
            (r'\s+', Whitespace)
        ],

        'double-quote': [
            (r'\{.*?\}', String.Interpol),
            (r'\\.', Literal.String.Escape),
            (r'[^"{}\\]+', String.Double),
            (r'"', String.Double, '#pop'),
        ]
    }