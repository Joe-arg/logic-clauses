class Atom:
    def __init__(self, name):
        self.name = name
        self.status = True

    def deny(self):
        self.status = not self.status

    def __str__(self):
        if self.status:
            return self.name
        else:
            return f"~{self.name}"
