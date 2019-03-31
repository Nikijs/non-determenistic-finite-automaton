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
            newNFA = nfa(nfa1.initial, nfa2.accept)
            nfastack.append(newNFA)

        elif c == '|':
            nfa2 = nfastack.pop()
            nfa1 = nfastack.pop()

            initial = state()
            
            initial.edge1 = nfa1.initial
            initial.edge2 = nfa2.initial

            accept = state()

            nfa1.accept.edge1 = accept
            nfa2.accept.edge1 = accept

            newNFA = nfa(initial, accept)
            nfastack.append(newNFA)

        elif c == '*':
            nfa1 = nfastack.pop()

            initial = state()
            accept = state()

            initial.edge1 = nfa1.initial
            initial.edge2 = accept

            nfa1.accept.edge1 = nfa.initial
            nfa.accept.edge2 = accept

            newNFA = nfa(initial, accept)
            nfastack.append(newNFA)
        else:
            accept = state()
            initial = state()
            initial.label = c
            initial.edge1 = accept
            newNFA = nfa(initial, accept)
            nfastack.append(newNFA)

#should only have 1 nfa on the stack
    return nfastack.pop()