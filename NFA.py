#NFA

def shuntingAlg(infix):
    specials = {'*': 50, '.': 40, '|': 30}

    stack = ""
    pofix = ""
    
    for c in infix:
        if c == '(':
            stack = stack + c
        elif c == ')':
            while stack[-1] != '(':
                pofix, stack = pofix + stack[-1], stack[:-1]
            stack = stack[:-1]
        elif c in specials:
            while stack and specials.get(c, 0) <= specials.get(stack[-1], 0):
                pofix, stack = pofix + stack[-1], stack[:-1]
            stack = stack + c
        else:
            pofix = pofix + c

    while stack:
        pofix, stack = pofix + stack[-1], stack[:-1]
             
    return pofix


class state:
    label = None
    edge1 = None
    edge2 = None

class nfa:
    initial = None
    accept = None

    def __init__(self, initial, accept):
        self.initial = initial
        self.accept = accept

def compile(pofix):
    nfastack = []

    for c in pofix:
        if c == '.':

        elif c == '|'

        elif c == '*'

        else:
            accept = state()
            initial = state()
            initial.label = c
            initial.edge1 = accept
            nfastack.append(nfa(initial, accept))