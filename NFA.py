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
    #constructor
    def __init__(self, initial, accept):
        self.initial = initial
        self.accept = accept

def compile(pofix):
    nfastack = []

    for c in pofix:
        if c == '.':
            nfa2 = nfastack.pop()
            nfa1 = nfastack.pop()
            nfa1.accept.edge1 = nfa2.initial
            nfastack.append(nfa1.initial, nfa2.accept)
        elif c == '|'
            nfa2 = nfastack.pop()
            nfa1 = nfastack.pop()

            initial = state()
            
            initial.edge1 = nfa1.initial
            initial.edge2 = nfa2.initial

            accept = state()

            nfa.accept.edge1 = accept
            nfa2.accept.edge1 = accept

            nfa.append(nfa(initial, accept))
        elif c == '*'

        else:
            accept = state()
            initial = state()
            initial.label = c
            initial.edge1 = accept
            nfastack.append(nfa(initial, accept))