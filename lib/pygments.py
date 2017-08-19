from pygments.lexer import RegexLexer, bygroups
from pygments import token


class FranzLexer(RegexLexer):
    name = 'Franz Lexer'
    tokens = {
        'root': [
            (r'"', token.String.Double, 'double-quote'),
            (r'[0-9]+(\.[0-9]+)?', token.Number),
            (r'\b(if|else|for|while|in|to|fn|ⲗ|try|rescue|assert|include|yield|return|break|continue)\b', token.Keyword.Reserved),
            (r'\b(int|str|any|float|list|dict|bool)\b', token.Keyword.Type),
            (r'\b(and|or|not)\b', token.Operator.Word),
            (r'\b([*+\-^=<>%/]+)\b', token.Operator),
            (r'#.*?$', token.Comment.Single),
            (r'([a-zA-Z][a-zA-Z0-9_!?\-%$]*)(\s*)(=)(\s*)(fn)',
                bygroups(token.Name.Function, token.Whitespace, token.Operator, token.Whitespace, token.Keyword.Reserved))
        ],

        'double-quote': [
            (r'\{.*?\}', token.String.Interpol),
            (r'[^"{}]+', token.String.Double),
            (r'"', token.String.Double, '#pop'),
        ]
    }