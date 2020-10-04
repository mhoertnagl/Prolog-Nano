import unittest
from nano.compiler.parser import parser
from nano.compiler.program import Program


class ParserTest(unittest.TestCase):
    def test_parse_empty(self):
        s = ''
        exp = Program()
        act = parser.parse(s)
        self.assertEqual(act.rules, exp.rules)
        self.assertEqual(act.queries, exp.queries)

    def test_parse_single_fact(self):
        s = 'sokrates.'
        exp = Program()
        exp.rules = [
            (('term', 'sokrates', []), [])
        ]
        act = parser.parse(s)
        self.assertEqual(act.rules, exp.rules)
        self.assertEqual(act.queries, exp.queries)

    def test_parse_multiple_facts(self):
        s = '''
            sokrates.
            human(plato).
        '''
        exp = Program()
        exp.rules = [
            (('term', 'sokrates', []), []),
            (('term', 'human', [('term', 'plato', [])]), []),
        ]
        act = parser.parse(s)
        self.assertEqual(act.rules, exp.rules)
        self.assertEqual(act.queries, exp.queries)

    def test_parse_single_rule(self):
        s = 'mortal(X) :- human(X).'
        exp = Program()
        exp.rules = [
            (
                ('term', 'mortal', [('var', 'X_0')]), 
                [('term', 'human', [('var', 'X_0')])]
            )
        ]
        act = parser.parse(s)
        self.assertEqual(act.rules, exp.rules)
        self.assertEqual(act.queries, exp.queries)

    def test_parse_single_query(self):
        s = '?- human(X).'
        exp = Program()
        exp.queries = [
            ('term', 'human', [('var', 'X')])
        ]
        act = parser.parse(s)
        self.assertEqual(act.rules, exp.rules)
        self.assertEqual(act.queries, exp.queries)
