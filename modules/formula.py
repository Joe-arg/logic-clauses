class Formula:
    def __init__(self):
        self.clauses = []
        self.certificate = {}

    def add_clause(self, clause):
        self.clauses.append(clause)

    def not_self(self):
        pass

    def or_with(self, formula):
        pass

    def and_with(self, formula):
        f = Formula()
        for c in self.clauses:
            f.add_clause(c.get_clone())
        for c in formula.clauses:
            f.add_clause(c.get_clone())
        return f

    def __str__(self):
        names = []
        for clause in self.clauses:
            names.append(str(clause))
        string = "[" + " ".join(names) + "]"
        return string
