from nano.compiler.parser import parser
from nano.solver import solve
from nano.solver.solutions import compress, restrict
from nano.utils import vars
from nano.solver.pretty import prettify

rules = []


def search(source):
    global rules
    prog = parser.parse(source)
    rules += prog.rules
    for query in prog.queries:
        vs = vars(query)
        for sol in solve(rules, query):
            sol = compress(sol)
            sol = restrict(sol, vs)
            yield prettify(sol)
