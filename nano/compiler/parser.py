import ply.yacc as yacc
from nano.compiler.lexer import tokens
from nano.compiler.program import Program


# program : query program
def p_program_query(p):
    'program : query program'
    p[0] = p[2].prepend_query(p[1])


#         | rule program
def p_program_rule(p):
    'program : rule program'
    p[0] = p[2].prepend_rule(p[1])


#         | EOF
def p_program_empty(p):
    'program : '
    p[0] = Program()


# query : '?-' term '.'
def p_query(p):
    'query : QUERY term PERIOD'
    p[0] = p[2]


# rule : term :- terms '.'
def p_rule_consequence(p):
    'rule : term TURNSTILE terms PERIOD'
    p[0] = (p[1], p[3])


#      | term '.'
def p_rule_fact(p):
    'rule : term PERIOD'
    p[0] = (p[1], [])


# terms : term ',' terms
def p_terms_list(p):
    'terms : term COMMA terms'
    p[0] = [p[1]] + p[3]


#       | term
def p_terms_base(p):
    'terms : term'
    p[0] = [p[1]]


# term : PREDICATE '(' terms ')'
def p_term_predicate(p):
    'term : PREDICATE LPAREN terms RPAREN'
    p[0] = ('term', p[1], p[3])


#      | PREDICATE
def p_term_constant(p):
    'term : PREDICATE'
    p[0] = ('term', p[1], [])


#      | VARIABLE
def p_term_variable(p):
    'term : VARIABLE'
    p[0] = ('var', p[1])


def p_error(p):
    print("Syntax error in input!")


parser = yacc.yacc()
