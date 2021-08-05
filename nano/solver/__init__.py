from copy import deepcopy
from nano.solver.unify import unify

def solve(db, qry):
    yield from _solve(db, qry, {}, 0)
    yield None


def _solve(db, qry, mgu, indent):
    for hd, tl in db:
        # Copy original MGU. For each fact or rule in the DB start with
        # the same MGU.
        mguc = deepcopy(mgu)
        # Unify the head. If it is a fact, we are done at this point.
        mguc = unify(hd, qry, mguc)
        # If unification failed, continue with the next fact or rule.
        if mguc is None:
            # print(' ' * indent, 'FAIL ', prettify_rule(hd, tl))
            continue
        yield from _solve_conjuction(db, tl, mguc, indent + 2)


def _solve_conjuction(db, clauses, mgu, indent):
    if len(clauses) == 0:
        yield mgu
    else:
        hd, *tl = clauses
        for sol in _solve(db, hd, mgu, indent):
            if sol is None:
                break
            yield from _solve_conjuction(db, tl, sol, indent)
