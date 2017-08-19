from pygments.lexer import RegexLexer, bygroups
from pygments.style import Style
from pygments.styles.default import DefaultStyle

from pygments.token import *


class ReplStyle(Style):
    styles = {}
    styles.update(DefaultStyle.styles)
    styles.update({
        Comment: '#75715e',
        Comment.Hashbang: '#665555',
        Comment.Multiline: '',
        Comment.Preproc: '',
        Comment.PreprocFile: '',
        Comment.Single: '',
        Comment.Special: '',
        Error: '#960050 bg:#1e0010',
        Escape: '',
        Generic: '',
        Generic.Deleted: '#f92672',
        Generic.Emph: 'italic',
        Generic.Error: '',
        Generic.Heading: '',
        Generic.Inserted: '#a6e22e',
        Generic.Output: '',
        Generic.Prompt: '',
        Generic.Strong: 'bold',
        Generic.Subheading: '#75715e',
        Generic.Traceback: '',
        Keyword: '#66d9ef',
        Keyword.Constant: '',
        Keyword.Declaration: '',
        Keyword.Namespace: '#f92672',
        Keyword.Pseudo: '',
        Keyword.Reserved: '',
        Keyword.Type: '',
        Literal: '#ae81ff',
        Literal.Date: '#e6db74',
        Literal.Number: '#ae81ff',
        Literal.Number.Bin: '',
        Literal.Number.Float: '',
        Literal.Number.Hex: '',
        Literal.Number.Integer: '',
        Literal.Number.Integer.Long: '',
        Literal.Number.Oct: '',
        Literal.String: '#665588',
        Literal.String.Affix: '',
        Literal.String.Backtick: '',
        Literal.String.Char: '',
        Literal.String.Delimiter: '',
        Literal.String.Doc: '',
        Literal.String.Double: '',
        Literal.String.Escape: '#ae81ff',
        Literal.String.Heredoc: '',
        Literal.String.Interpol: '#898989',
        Literal.String.Other: '',
        Literal.String.Regex: '',
        Literal.String.Single: '',
        Literal.String.Symbol: '',
        Name: '#f0f0f2 italic',
        Name.Attribute: '#a6e22e',
        Name.Builtin: '',
        Name.Builtin.Pseudo: '',
        Name.Class: '#a6e22e',
        Name.Constant: '#66d9ef',
        Name.Decorator: '#a6e22e',
        Name.Entity: '',
        Name.Exception: '#a6e22e',
        Name.Function: '#a6e22e',
        Name.Function.Magic: '',
        Name.Label: '',
        Name.Namespace: '',
        Name.Other: '#a6e22e',
        Name.Property: '',
        Name.Tag: '#f92672',
        Name.Variable: '',
        Name.Variable.Class: '',
        Name.Variable.Global: '',
        Name.Variable.Instance: '',
        Name.Variable.Magic: '',
        Operator: '#f92672',
        Operator.Word: '',
        Other: '',
        Punctuation: '#fefefe',
        Text: '#f8f8f2',
        Text.Whitespace: ''
    })


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
            (r'\b[a-zA-Z][a-zA-Z0-9_!?\-%$]*\b', Name),
            (r'\s+([*+\-^=<>%/]+)\s+', Operator),
        ],

        'double-quote': [
            (r'\{.*?\}', String.Interpol),
            (r'[^"{}]+', String.Double),
            (r'"', String.Double, '#pop'),
        ]
    }