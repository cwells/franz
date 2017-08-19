from pygments.lexer import RegexLexer, bygroups
from pygments.style import Style
from pygments.styles.default import DefaultStyle
from pygments.styles.monokai import MonokaiStyle
from pygments.token import (
    Keyword, Name, Comment, String, Error,
    Number, Operator, Generic, Whitespace
)

class ReplStyle(Style):
    styles = {}
    styles.update(MonokaiStyle.styles)
    # styles.update({
    #     Comment:        '#cedad2 italic',
    #     Keyword:        '#9fb8bb bold',
    #     Keyword.Type:   '#729ca8',
    #     Operator:       '#9cae81 bold',
    #     # Name.Function:  '#',
    # })


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
                bygroups(Name.Function, Whitespace, Operator, Whitespace, Keyword.Reserved)),
            (r'\s+([*+\-^=<>%/]+)\s+', Operator),
        ],

        'double-quote': [
            (r'\{.*?\}', String.Interpol),
            (r'[^"{}]+', String.Double),
            (r'"', String.Double, '#pop'),
        ]
    }