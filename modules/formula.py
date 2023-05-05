from modules.atom import Atom
from modules.clause import Clause


class Formula:
    def __init__(self):
        self.clauses = []
        self.cert = {}
        self.forks = 0

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
                add = True
                for a in cb.atoms.values():
                    add = c.add_atom(a.get_clone()) and add
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
        empty_clause = False
        for c in self.clauses:
            if not c.atoms:
                empty_clause = True
                break
        if empty_clause:
            if self.forks == 1:
                return self.fork()
            else:
                return False
        elif self.clauses:
            if self.unit_clauses() or self.pure_literal():
                return self.davis_putnam()
            else:
                return self.fork()
        else:
            return True

    def fork(self):
        try:
            a = list(self.clauses[0].atoms.values())[0]
        except:
            return False
        f1 = self.get_clone()
        a = a.get_clone()
        f1.cert[a.name] = a
        f1.simplify(a)
        if f1.davis_putnam():
            return True
        f2 = self.get_clone()
        a = a.get_clone()
        a.negate()
        f2.cert[a.name] = a
        f2.simplify(a)
        return f2.davis_putnam()

    def unit_clauses(self):
        enter = False
        uc = [c for c in self.clauses if len(c.atoms) == 1]
        while uc:
            enter = True
            a = list(uc[0].atoms.values())[0]
            self.cert[a.name] = a
            self.simplify(a)
            uc = [c for c in self.clauses if len(c.atoms) == 1]
        return enter

    def pure_literal(self):
        enter = False
        pl = {}
        for c in self.clauses:
            for a in c.atoms.values():
                if a.name in pl:
                    if a.status != pl[a.name]:
                        pl[a.name] = None
                else:
                    pl[a.name] = a.status
        for name, status in pl.items():
            if status is not None:
                enter = True
                a = Atom(name)
                a.status = status
                self.cert[name] = a
                self.simplify(a)
        return enter

    def simplify(self, a):
        sf = []
        for c in self.clauses:
            if a.name not in c.atoms:
                sf.append(c)
            elif a.status != c.atoms[a.name].status:
                del c.atoms[a.name]
                sf.append(c)
        self.clauses = sf

    def get_clone(self):
        f = Formula()
        f.cert = self.cert
        f.forks = self.forks + 1
        for c in self.clauses:
            f.add_clause(c.get_clone())
        return f

    def print_cert(self):
        names = []
        for atom in self.cert.values():
            names.append(str(atom))
        print(', '.join(names))

    def __str__(self):
        names = []
        for clause in self.clauses:
            names.append(str(clause))
        string = "[" + " ".join(names) + "]"
        return string
