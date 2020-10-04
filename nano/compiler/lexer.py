import ply.lex as lex

tokens = (
    'VARIABLE',
    'PREDICATE',
    'LPAREN',
    'RPAREN',
    'COMMA',
    'PERIOD',
    'TURNSTILE',
    'QUERY',
)

t_VARIABLE = r'_|[A-Z][a-zA-Z0-9]*'
t_PREDICATE = r'[a-z][a-zA-Z0-9]*'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_PERIOD = r'\.'
t_TURNSTILE = r':-'
t_QUERY = r'\?-'

t_ignore = ' \t'
t_ignore_COMMENT = r'%.*'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()
