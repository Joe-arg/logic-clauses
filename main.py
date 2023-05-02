import re

from modules.atom import Atom
from modules.clause import Clause
from modules.formula import Formula


def get_priority(o):
    match o:
        case '|':
            return 1
        case '&':
            return 2
        case '>':
            return 3
        case '=':
            return 4
        case '~':
            return 5
        case '(':
            return -1
        case ')':
            return -2
    return 0


def infix_to_postfix(infix):
    postfix = []
    stack = []
    for o in infix:
        p = get_priority(o)
        if p == -1:
            stack.append(o)
        elif p == -2:
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            if stack:
                stack.pop()
        elif p:
            if not stack or p > get_priority(stack[-1]):
                stack.append(o)
            else:
                while stack and p < get_priority(stack[-1]):
                    postfix.append(stack.pop())
                stack.append(o)
        else:
            postfix.append(o)
    while stack:
        postfix.append(stack.pop())
    return postfix


def evaluate_postfix(postfix):
    stack = []
    for o in postfix:
        p = get_priority(o)
        if p == 0:
            a = Atom(o)
            c = Clause()
            f = Formula()
            c.add_atom(a)
            f.add_clause(c)
            stack.append(f)
        elif p == 1:
            b = stack.pop()
            a = stack.pop()
            c = a.disjunction(b)
            stack.append(c)
        elif p == 2:
            b = stack.pop()
            a = stack.pop()
            c = a.conjunction(b)
            stack.append(c)
        elif p == 3:
            b = stack.pop()
            a = stack.pop()
            c = a.negate().disjunction(b)
            stack.append(c)
        elif p == 4:
            b = stack.pop()
            a = stack.pop()
            c = a.negate().disjunction(b)
            d = b.negate().disjunction(a)
            e = c.conjunction(d)
            stack.append(e)
        elif p == 5:
            a = stack.pop()
            a = a.negate()
            stack.append(a)
    return stack.pop()


pattern = r'\||&|>|=|~|\(|\)|\w+'
file = open("data/formula1")
lines = file.readlines()
for line in lines:
    infix = re.findall(pattern, line)
    print(infix)
    postfix = infix_to_postfix(infix)
    print(postfix)
    formula = evaluate_postfix(postfix)
    print(formula)
    c = Clause()
    c.add_atom(Atom('c'))
    formula.add_clause(c)
    print(formula)
    print(formula.unit_clauses())
    print(formula)
    print(formula.cert)
