from nano.utils import is_var, name, is_term, is_const, clauses


def prettify(sol, inline=False):
    if sol == None:
        return 'no'
    elif len(sol) == 0:
        return 'yes'
    else:
        sols = map(prettify_binding, sol.items())
        delim = '\n'
        if inline:
            delim = ', '
        return delim.join(sols)


def prettify_binding(b):
    return '{} = {}'.format(b[0], prettify_term(b[1]))


def prettify_term(t):
    if is_var(t):
        return name(t)
    elif is_const(t):
        return name(t)
    elif is_term(t):
        cs = prettify_terms(clauses(t))
        return '{}({})'.format(name(t), cs)
    return ''


def prettify_terms(ts):
    return ', '.join(map(prettify_term, ts))


# DEBUG
def prettify_rule(hd, tl):
    txt = prettify_term(hd)
    if tl:
        txt += ' :- '
        txt += prettify_terms(tl)
    txt += '.'
    return txt