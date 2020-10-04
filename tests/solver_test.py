import unittest
from nano.compiler.parser import parser
from nano.solver import solve


class SolverTest(unittest.TestCase):
    def test_solve_fail(self):
        src = '''
            human(sokrates).
            human(plato).
            god(zeus).
            ?- mortal(zeus).
        '''
        db = parser.parse(src)
        gen = solve(db.rules, db.queries[0])
        # Assertions
        exp = None
        self.assertEqual(next(gen), exp)

    def test_solve_facts_list(self):
        src = '''
            human(sokrates).
            human(plato).
            god(zeus).
            ?- human(X).
        '''
        db = parser.parse(src)
        gen = solve(db.rules, db.queries[0])
        # Assertions
        exp = {'X': ('term', 'sokrates', [])}
        self.assertEqual(next(gen), exp)
        exp = {'X': ('term', 'plato', [])}
        self.assertEqual(next(gen), exp)
        exp = None
        self.assertEqual(next(gen), exp)

    def test_solve_single_clause1(self):
        src = '''
            human(sokrates).
            human(plato).
            god(zeus).
            mortal(X) :- human(X).
            ?- mortal(sokrates).
        '''
        db = parser.parse(src)
        gen = solve(db.rules, db.queries[0])
        # Assertions
        exp = {'X_0': ('term', 'sokrates', [])}
        self.assertEqual(next(gen), exp)
        exp = None
        self.assertEqual(next(gen), exp)

    def test_solve_single_clause2(self):
        src = '''
            human(sokrates).
            human(plato).
            god(zeus).
            mortal(X) :- human(X).
            ?- mortal(X).
        '''
        db = parser.parse(src)
        gen = solve(db.rules, db.queries[0])
        # Assertions
        exp = {'X': ('var', 'X_0'), 'X_0': ('term', 'sokrates', [])}
        self.assertEqual(next(gen), exp)
        exp = {'X': ('var', 'X_0'), 'X_0': ('term', 'plato', [])}
        self.assertEqual(next(gen), exp)
        exp = None
        self.assertEqual(next(gen), exp)

    def test_solve_single_clause3(self):
        src = '''
            human(sokrates).
            human(plato).
            god(zeus).
            mortal(X) :- human(X).
            ?- mortal(Y).
        '''
        db = parser.parse(src)
        gen = solve(db.rules, db.queries[0])
        # Assertions
        exp = {'X_0': ('var', 'Y'), 'Y': ('term', 'sokrates', [])}
        self.assertEqual(next(gen), exp)
        exp = {'X_0': ('var', 'Y'), 'Y': ('term', 'plato', [])}
        self.assertEqual(next(gen), exp)
        exp = None
        self.assertEqual(next(gen), exp)

    def test_solve_double_clause(self):
        src = '''
            human(sokrates).
            deity(zeus).
            male(sokrates).
            male(zeus).
            god(X) :- male(X), deity(X).
            ?- god(X).
        '''
        db = parser.parse(src)
        gen = solve(db.rules, db.queries[0])
        # Assertions
        exp = {'X': ('var', 'X_0'), 'X_0': ('term', 'zeus', [])}
        self.assertEqual(next(gen), exp)
        exp = None
        self.assertEqual(next(gen), exp)

    def test_solve_double_clause2(self):
        src = '''
            parent(zeus, chronos).
            parent(zeus, rhea).
            parent(athena, zeus).
            grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
            ?- grandparent(X, Y).
        '''
        db = parser.parse(src)
        gen = solve(db.rules, db.queries[0])
        # Assertions
        exp = {
            'X': ('var', 'X_0'),
            'X_0': ('term', 'athena', []),
            'Y': ('var', 'Y_0'),
            'Y_0': ('term', 'chronos', []),
            'Z_0': ('term', 'zeus', [])
        }
        self.assertEqual(next(gen), exp)
        exp = {
            'X': ('var', 'X_0'),
            'X_0': ('term', 'athena', []),
            'Y': ('var', 'Y_0'),
            'Y_0': ('term', 'rhea', []),
            'Z_0': ('term', 'zeus', [])
        }
        self.assertEqual(next(gen), exp)
        # exp = None
        # self.assertEqual(next(gen), exp)

    def test_solve_nested_clause(self):
        src = '''
            male(zeus).
            male(chronos).
            female(rhea).
            female(athena).
            parent(zeus, chronos).
            parent(zeus, rhea).
            parent(athena, zeus).
            grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
            grandfather(X, Z) :- grandparent(X, Z), male(Z).
            ?- grandfather(X, Z).
        '''
        db = parser.parse(src)
        gen = solve(db.rules, db.queries[0])
        # Assertions
        exp = {
            'X': ('var', 'X_0'),
            'X_0': ('var', 'X_1'),
            'X_1': ('term', 'athena', []),
            'Y_1': ('term', 'zeus', []),
            'Z': ('var', 'Z_0'),
            'Z_0': ('var', 'Z_1'),
            'Z_1': ('term', 'chronos', []),
        }
        self.assertEqual(next(gen), exp)
        exp = None
        self.assertEqual(next(gen), exp)

    def test_solve_nested_clause2(self):
        src = '''
            male(zeus).
            male(chronos).
            female(rhea).
            female(athena).
            parent(zeus, chronos).
            parent(zeus, rhea).
            parent(athena, zeus).
            father(X, Y) :- parent(X, Y), male(Y).
            grandfather(X, Z) :- parent(X, Y), father(Y, Z).
            ?- grandfather(X, Z).
        '''
        db = parser.parse(src)
        gen = solve(db.rules, db.queries[0])
        # Assertions
        exp = {
            'X': ('var', 'X_0'),
            'X_0': ('term', 'athena', []),
            'X_1': ('term', 'zeus', []),
            'Y_0': ('term', 'zeus', []),
            'Y_1': ('var', 'Z_0'),
            'Z': ('var', 'Z_0'),
            'Z_0': ('term', 'chronos', []),
        }
        self.assertEqual(next(gen), exp)
        exp = None
        self.assertEqual(next(gen), exp)
