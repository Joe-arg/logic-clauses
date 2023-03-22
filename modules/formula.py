class Formula:
    def __init__(self):
        self.clauses = []

    def add_clause(self, clause):
        self.clauses.append(clause)

    def __str__(self):
        names = []
        for clause in self.clauses:
            names.append(str(clause))
        string = "[" + " ".join(names) + "]"
        return string