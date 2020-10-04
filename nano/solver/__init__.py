from copy import deepcopy
from nano.solver.unify import unify

# from nano.solver.pretty import prettify, prettify_term, prettify_terms, prettify_rule


def solve(db, qry):
    # print()
    # print('=' * 80)
    yield from _solve(db, qry, {}, 0)
    yield None


def _solve(db, qry, mgu, indent):
    # print('-' * 80)
    # print('QRY: ', prettify_term(qry))
    # print('MGU: ', prettify(mgu, True))
    # print('-' * 80)
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
        # else:
        #     print(' ' * indent, '     ', prettify_rule(hd, tl))
        #     print(' ' * indent, '     ', prettify(mguc, True))

        # if tl:
        #     print(' ' * indent, 'CONJ BEGIN')
        yield from _solve_conjuction(db, tl, mguc, indent + 2)
        # if tl:
        #     print(' ' * indent, 'CONJ END')


def _solve_conjuction(db, clauses, mgu, indent):
    if len(clauses) == 0:
        yield mgu
    else:
        hd, *tl = clauses
        for sol in _solve(db, hd, mgu, indent):
            if sol is None:
                break
            yield from _solve_conjuction(db, tl, sol, indent)
