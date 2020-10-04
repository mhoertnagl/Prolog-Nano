def is_var(t):
    return t[0] == 'var'


def is_term(t):
    return t[0] == 'term'


def name(t):
    return t[1]


def arity(t):
    return len(t[2])


def is_const(t):
    return is_term(t) and arity(t) == 0


def clauses(t):
    return t[2]


def head(r):
    return r[0]


def tail(r):
    return r[1]


def vars(t):
    if t is None:
        return None
    elif is_var(t):
        return {name(t)}
    elif is_term(t):
        cs = map(vars, clauses(t))
        return set.union(*cs)
    return {}
