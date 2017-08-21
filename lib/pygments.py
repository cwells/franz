from pygments.lexer import RegexLexer, bygroups
from pygments.style import Style
from pygments.token import *

from .termcolors import termcolors

COMMENT = "%(Grey27)s" % termcolors
KEYWORD = "%(PaleTurquoise4)s" % termcolors
TYPE = "%(SlateBlue3)s" % termcolors
LITERAL = "%(Grey85)s" % termcolors
NAME = "%(Plum4)s italic" % termcolors
FUNCTION = "%(SteelBlue)s italic" % termcolors
FUNCTION_DEF = "%(SteelBlue3)s italic" % termcolors
NUMBER = "%(Silver)s" % termcolors
STRING = "%(Grey)s" % termcolors
STRING_ESCAPE = "%(DarkRed)s" % termcolors
STRING_INTERPOL = NAME
OPERATOR = "%(Orange4)s" % termcolors
OPERATOR_WORD = "%(Orange4)s" % termcolors
PUNCTUATION = "%(Grey42)s" % termcolors
BRACES = "%(Grey50)s" % termcolors
TEXT = "%(Grey46)s" % termcolors

class ReplStyle(Style):
    styles = {
        Comment: COMMENT,
        Comment.Hashbang: '',
        Comment.Multiline: '',
        Comment.Preproc: '',
        Comment.PreprocFile: '',
        Comment.Single: COMMENT,
        Comment.Special: '',
        Error: '#960050 bg:#1e0010',
        Escape: '',
        Generic: '',
        Generic.Deleted: '',
        Generic.Emph: 'italic',
        Generic.Error: '',
        Generic.Heading: '',
        Generic.Inserted: '',
        Generic.Output: '',
        Generic.Prompt: '',
        Generic.Strong: 'bold',
        Generic.Subheading: '',
        Generic.Traceback: '',
        Keyword: KEYWORD,
        Keyword.Constant: '',
        Keyword.Declaration: '',
        Keyword.Namespace: '',
        Keyword.Pseudo: '',
        Keyword.Reserved: KEYWORD,
        Keyword.Type: TYPE,
        Literal: LITERAL,
        Literal.Date: '',
        Literal.Number: NUMBER,
        Literal.Number.Bin: '',
        Literal.Number.Float: '',
        Literal.Number.Hex: '',
        Literal.Number.Integer: '',
        Literal.Number.Integer.Long: '',
        Literal.Number.Oct: '',
        Literal.String: STRING,
        Literal.String.Affix: '',
        Literal.String.Backtick: '',
        Literal.String.Char: '',
        Literal.String.Delimiter: '',
        Literal.String.Doc: '',
        Literal.String.Double: '',
        Literal.String.Escape: STRING_ESCAPE,
        Literal.String.Heredoc: '',
        Literal.String.Interpol: STRING_INTERPOL,
        Literal.String.Other: '',
        Literal.String.Regex: '',
        Literal.String.Single: '',
        Literal.String.Symbol: '',
        Name: NAME,
        Name.Attribute: '',
        Name.Builtin: '',
        Name.Builtin.Pseudo: '',
        Name.Class: '',
        Name.Constant: '',
        Name.Decorator: '',
        Name.Entity: '',
        Name.Exception: '',
        Name.Function: FUNCTION,
        Name.Function.Definition: FUNCTION_DEF,
        Name.Function.Magic: '',
        Name.Label: '',
        Name.Namespace: '',
        Name.Other: '',
        Name.Property: '',
        Name.Tag: '',
        Name.Variable: '',
        Name.Variable.Class: '',
        Name.Variable.Global: '',
        Name.Variable.Instance: '',
        Name.Variable.Magic: '',
        Operator: OPERATOR,
        Operator.Word: OPERATOR_WORD,
        Other: '',
        Punctuation: PUNCTUATION,
        Punctuation.Braces: BRACES,
        String.Double: STRING,
        Text: TEXT,
        Text.Whitespace: ''
    }


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