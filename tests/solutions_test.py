import unittest
from nano.solver.solutions import compress, restrict


class SolutionsTest(unittest.TestCase):
    def test_compress(self):
        mgu = {
            'X' : ('var', 'Y'),
            'Y' : ('var', 'Z'),
            'Z' : ('term', 'sokrates', []),
            'A' : ('var', 'B'),
            'C' : ('term', 'plato', []),
        }
        exp = {
            'X' : ('term', 'sokrates', []),
            'Y' : ('term', 'sokrates', []),
            'Z' : ('term', 'sokrates', []),
            'A' : ('var', 'B'),
            'C' : ('term', 'plato', []),            
        }
        act = compress(mgu)
        self.assertEqual(act, exp)