from nano.utils import is_var, name, is_term, arity, clauses

def unify(t1, t2, mgu):
    """
    Unifies terms t1 and t2 and returns the most general unifier if it exists.
    Returns None otherwise.

    >>> unify(
    ...     ('term', 'human', [('term', 'sokrates', [])]),
    ...     ('term', 'human', [('var', 'X')]))
    {'X': ('term', 'sokrates', [])}

    Two equal terms will yield an empty unifier. For instance

    >>> unify(
    ...     ('term', 'sokrates', []),
    ...     ('term', 'sokrates', []))
    {}

    Equal terms can always be unified. Whereas

    >>> unify(
    ...     ('term', 'sokrates', []),
    ...     ('term', 'plato', []))
    None

    These two terms cannot be unified and unify returns None.
    """
    queue = [(t1, t2)]
    while queue:
        q1, q2 = queue.pop(0)
        
        while is_var(q1) and (name(q1) in mgu):
            q1 = mgu[name(q1)]
        while is_var(q2) and (name(q2) in mgu):
            q2 = mgu[name(q2)]

        if is_var(q1) and is_var(q2):
            if name(q1) < name(q2):
                mgu[name(q1)] = q2
            elif name(q1) > name(q2):
                mgu[name(q2)] = q1
            else:
                continue
        elif is_var(q1):
            mgu[name(q1)] = q2
        elif is_var(q2): 
            mgu[name(q2)] = q1
        elif is_term(q1) and is_term(q2):
            if name(q1) == name(q2) and arity(q1) == arity(q2):
                c1 = clauses(q1)
                c2 = clauses(q2)
                queue += zip(c1, c2)
            else:
                return None
        else:
            return None
    return mgu

