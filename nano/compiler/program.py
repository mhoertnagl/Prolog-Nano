from nano.utils import is_var, name, is_term, clauses, head, tail


class Program(object):
    def __init__(self):
        self.counter = 0
        self.rules = []
        self.queries = []

    def prepend_rule(self, rule):
        rule = self.rename_rule(rule)
        self.rules.insert(0, rule)
        self.counter += 1
        return self

    def prepend_query(self, query):
        self.queries.insert(0, query)
        return self

    def rename_rule(self, rule):
        hd = self.rename_term(head(rule))
        tl = map(self.rename_term, tail(rule))
        return (hd, list(tl))

    def rename_term(self, term):
        if is_var(term):
            nm = '{}_{}'.format(name(term), self.counter)
            return ('var', nm)
        elif is_term(term):
            cs = map(self.rename_term, clauses(term))
            return ('term', name(term), list(cs))
        else:
            return None
