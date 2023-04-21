class Clause:
    def __init__(self):
        self.atoms = {}

    def add_atom(self, atom):
        self.atoms[atom.name] = atom

    def get_clone(self):
        c = Clause()
        for a in self.atoms.values():
            c.add_atom(a.get_clone())
        return c

    def __str__(self):
        names = []
        for atom in self.atoms.values():
            names.append(str(atom))
        string = "(" + " | ".join(names) + ")"
        return string
