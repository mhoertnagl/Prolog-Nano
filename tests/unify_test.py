import unittest
from nano.solver.unify import unify


class UnifyTest(unittest.TestCase):
    def test_unify_same_vars(self):
        t1 = ('var', 'X')
        t2 = ('var', 'X')
        exp = {}
        act = unify(t1, t2, {})
        self.assertEqual(act, exp)

    def test_unify_different_vars1(self):
        t1 = ('var', 'X')
        t2 = ('var', 'Y')
        exp = {'X': ('var', 'Y')}
        act = unify(t1, t2, {})
        self.assertEqual(act, exp)

    def test_unify_different_vars2(self):
        t1 = ('var', 'Y')
        t2 = ('var', 'X')
        exp = {'X': ('var', 'Y')}
        act = unify(t1, t2, {})
        self.assertEqual(act, exp)

    def test_unify_terms0(self):
        t1 = ('term', 'sokrates', [])
        t2 = ('term', 'sokrates', [])
        exp = {}
        act = unify(t1, t2, {})
        self.assertEqual(act, exp)

    def test_unify_terms1(self):
        t1 = ('term', 'human', [('term', 'sokrates', [])])
        t2 = ('var', 'X')
        exp = {'X': ('term', 'human', [('term', 'sokrates', [])])}
        act = unify(t1, t2, {})
        self.assertEqual(act, exp)

    def test_unify_terms2(self):
        t1 = ('term', 'human', [('term', 'sokrates', [])])
        t2 = ('term', 'human', [('var', 'X')])
        exp = {'X': ('term', 'sokrates', [])}
        act = unify(t1, t2, {})
        self.assertEqual(act, exp)

    def test_unify_terms3(self):
        t1 = ('term', 'teacher', [('term', 'sokrates', []),
                                  ('term', 'plato', [])])
        t2 = ('term', 'teacher', [('var', 'X'), ('var', 'Y')])
        exp = {'X': ('term', 'sokrates', []), 'Y': ('term', 'plato', [])}
        act = unify(t1, t2, {})
        self.assertEqual(act, exp)

    def test_unify_fail_terms1(self):
        t1 = ('term', 'sokrates', [])                                 
        t2 = ('term', 'plato', [])
        exp = None
        act = unify(t1, t2, {})
        self.assertEqual(act, exp)

    def test_unifyc_rhea(self):
        t1 = ('term', 'parent', [('var', 'Y'), ('var', 'Z')]) 
        t2 = ('term', 'parent', [
            ('term', 'zeus', []), 
            ('term', 'rhea', [])
        ])
        mgu = {
            # 'X': ('term', 'zeus', []),
            'Y': ('term', 'chronos', [])
        }
        exp = None
        act = unify(t1, t2, mgu)
        self.assertEqual(act, exp)

    # TODO: Failing unifications
    # TODO: Selfreferential unification X, f(X)
