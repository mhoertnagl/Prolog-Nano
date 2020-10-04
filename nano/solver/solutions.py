from nano.utils import is_var, name


def compress(mgu):
    if mgu is None:
        return None
    res = {}
    for v, t in mgu.items():
        while is_var(t) and (name(t) in mgu):
            t = mgu[name(t)]
        res[v] = t
    return res


def restrict(mgu, vars):
    if mgu is None:
        return None
    res = {}
    for v, t in mgu.items():
        if v in vars:
            res[v] = t
    return res
