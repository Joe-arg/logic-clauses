import re

from modules.atom import Atom
from modules.clause import Clause
from modules.formula import Formula

pattern = r'\||&|>|=|~|\(|\)|[a-zA-Z0-9]+'
file = open("data/formula1")
lines = file.readlines()
for line in lines:
    list = re.findall(pattern, line)
    print(list)
