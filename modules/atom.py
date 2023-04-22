class Atom:
    def __init__(self, name):
        self.name = name
        self.status = True

    def negate(self):
        self.status = not self.status

    def get_clone(self):
        a = Atom(self.name)
        a.status = self.status
        return a

    def __str__(self):
        if self.status:
            return self.name
        else:
            return f"~{self.name}"
