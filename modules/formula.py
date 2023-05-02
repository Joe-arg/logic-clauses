from modules.clause import Clause


class Formula:
    def __init__(self):
        self.clauses = []
        self.cert = {}

    def add_clause(self, clause):
        self.clauses.append(clause)

    def negate(self):
        f = []
        for c in self.clauses:
            fa = Formula()
            for a in c.atoms.values():
                a = a.get_clone()
                a.negate()
                ca = Clause()
                ca.add_atom(a)
                fa.add_clause(ca)
            f.append(fa)
        while len(f) > 1:
            a = f.pop(0)
            b = f.pop(0)
            f.insert(0, a.disjunction(b))
        return f.pop()

    def disjunction(self, formula):
        f = Formula()
        for ca in self.clauses:
            for cb in formula.clauses:
                c = ca.get_clone()
                add = False
                for a in cb.atoms.values():
                    add = c.add_atom(a.get_clone())
                if add:
                    f.add_clause(c)
        return f

    def conjunction(self, formula):
        f = Formula()
        for c in self.clauses:
            f.add_clause(c.get_clone())
        for c in formula.clauses:
            f.add_clause(c.get_clone())
        return f

    def davis_putnam(self):
        for c in self.clauses:
            pass

    def unit_clauses(self):
        f = Formula()
        uc = False
        for c in self.clauses:
            if len(c.atoms) == 1:
                uc = True
                a = list(c.atoms.values())[0]
                self.cert[a.name] = a
                self.remove_atom(a)
        return f if uc else None

    def pure_literal(self):
        pl = False
        for c in self.clauses:
            for a in c.atoms.values:
                pass

    def remove_atom(self, a):
        for c in self.clauses:
            if a.name in c.atoms:
                if a.status == c.atoms[a.name].status:
                    self.clauses.remove(c)
                else:
                    del c.atoms[a.name]

    def __str__(self):
        names = []
        for clause in self.clauses:
            names.append(str(clause))
        string = "[" + " ".join(names) + "]"
        return string
