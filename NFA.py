#NFA

def shuntingAlg(infix):
    #special characters with precedence
    specials = {'*': 50, '.': 40, '|': 30}

    stack = ""
    #operator stack
    pofix = ""
    #loop through the characters
    for c in infix:
        #push to the stack
        if c == '(':
            stack = stack + c
            #pop from stack
        elif c == ')':
            while stack[-1] != '(':
                pofix, stack = pofix + stack[-1], stack[:-1]
            stack = stack[:-1]
            #if operator push to stack after popping lower or equal precedence
        elif c in specials:
            while stack and specials.get(c, 0) <= specials.get(stack[-1], 0):
                pofix, stack = pofix + stack[-1], stack[:-1]
            stack = stack + c
            #regular characters pushed to stack
        else:
            pofix = pofix + c
            
    while stack:
        pofix, stack = pofix + stack[-1], stack[:-1]
             #return postfix regex
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
                nfa2
        elif c == '|'

        elif c == '*'

        else:
            accept = state()
            initial = state()
            initial.label = c
            initial.edge1 = accept
            nfastack.append(nfa(initial, accept))