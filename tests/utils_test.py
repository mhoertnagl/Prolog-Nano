import unittest
from nano.utils import vars


class UtilsTest(unittest.TestCase):
    def test_vars_empty(self):
        trm = None
        exp = None
        act = vars(trm)
        self.assertEqual(act, exp)

    def test_vars_var(self):
        trm = ('var', 'Y')
        exp = {'Y'}
        act = vars(trm)
        self.assertEqual(act, exp)

    def test_vars_term(self):
        trm = ('term', 'a', [
            ('term', 'b', [
                ('var', 'X'),
                ('var', 'Y'),
            ]),
            ('var', 'Y'),
        ])
        exp = {'X', 'Y'}
        act = vars(trm)
        self.assertEqual(act, exp)