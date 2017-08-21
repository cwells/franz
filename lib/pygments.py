from pygments.lexer import RegexLexer, bygroups
from pygments.style import Style

from pygments.token import *


class ReplStyle(Style):
    styles = {
        Comment: '#602222',
        Comment.Hashbang: '',
        Comment.Multiline: '',
        Comment.Preproc: '',
        Comment.PreprocFile: '',
        Comment.Single: '#602222',
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
        Keyword: '#7DA182',
        Keyword.Constant: '',
        Keyword.Declaration: '',
        Keyword.Namespace: '',
        Keyword.Pseudo: '',
        Keyword.Reserved: '#7DA182',
        Keyword.Type: '#A0998D',
        Literal: '#A0998D',
        Literal.Date: '',
        Literal.Number: '#AF944F',
        Literal.Number.Bin: '',
        Literal.Number.Float: '',
        Literal.Number.Hex: '',
        Literal.Number.Integer: '',
        Literal.Number.Integer.Long: '',
        Literal.Number.Oct: '',
        Literal.String: '#C2C1BD',
        Literal.String.Affix: '',
        Literal.String.Backtick: '',
        Literal.String.Char: '',
        Literal.String.Delimiter: '',
        Literal.String.Doc: '',
        Literal.String.Double: '',
        Literal.String.Escape: '#8a644a',
        Literal.String.Heredoc: '',
        Literal.String.Interpol: '#A5B288',
        Literal.String.Other: '',
        Literal.String.Regex: '',
        Literal.String.Single: '',
        Literal.String.Symbol: '',
        Name: '#529389 italic',
        Name.Attribute: '',
        Name.Builtin: '',
        Name.Builtin.Pseudo: '',
        Name.Class: '',
        Name.Constant: '',
        Name.Decorator: '',
        Name.Entity: '',
        Name.Exception: '',
        Name.Function: '#7D441D',
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
        Operator: '#D4C99C',
        Operator.Word: '#B9C2AA',
        Other: '#556699',
        Punctuation: '#7D441D',
        Punctuation.Braces: '#C6C1A8',
        String.Double: '#A0998D',
        Text: '#8C6B21',
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
                bygroups(Name.Function, Whitespace, Operator, Whitespace, Keyword.Reserved)),
            (r'\b[a-zA-Z][a-zA-Z0-9_!?\-%$]*\b', Name),
            (r'\s+([*+\-^=<>%/?]+)\s+', Operator),
            (r'[@().,:;\[\]]', Punctuation),
            (r'[{}]', Punctuation.Braces),
        ],

        'double-quote': [
            (r'\{.*?\}', String.Interpol),
            (r'\\.', Literal.String.Escape),
            (r'[^"{}\\]+', String.Double),
            (r'"', String.Double, '#pop'),
        ]
    }