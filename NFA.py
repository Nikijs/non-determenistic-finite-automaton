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
            #push nfa to stack
            newNFA = nfa(nfa1.initial, nfa2.accept)
            nfastack.append(newNFA)

        elif c == '|':
            nfa2 = nfastack.pop()
            nfa1 = nfastack.pop()
            #create new initial and accept states
            initial = state()
            
            initial.edge1 = nfa1.initial
            initial.edge2 = nfa2.initial

            accept = state()

            nfa1.accept.edge1 = accept
            nfa2.accept.edge1 = accept
            #push nfa to stack
            newNFA = nfa(initial, accept)
            nfastack.append(newNFA)

        elif c == '*':
            nfa1 = nfastack.pop()

            initial = state()
            accept = state()

            initial.edge1 = nfa1.initial
            initial.edge2 = accept

            nfa1.accept.edge1 = nfa1.initial
            nfa1.accept.edge2 = accept
            #push nfa to stack
            newNFA = nfa(initial, accept)
            nfastack.append(newNFA)
        else:
            accept = state()
            initial = state()
            initial.label = c
            initial.edge1 = accept
            #push nfa to stack
            newNFA = nfa(initial, accept)
            nfastack.append(newNFA)

#should only have 1 nfa on the stack
    return nfastack.pop()

def followes(state):
    #create new state
    states = set()
    states.add(state)

    #check if states have e arrows 
    if state.label is None:
        if state.edge1 is not None:
            #if edge1 follow
            states = states | followes(state.edge1)
        if state.edge2 is not None:
            #if edge1 follow    
            states = states | followes(state.edge2)


    return states

def match(infix, string):
    #convert infix to postfix and compile regular expression
    postfix = shuntingAlg(infix)
    nfa = compile(postfix)

    current = set()
    next = set()
    
    current = current | followes(nfa.initial)

    #loop through each char in string 
    for s in string:
        #loop through the set of states
        for c in current:
            #check if state is s
            if c.label == s:
                #add edge1 state to the next set
                next = next | followes(c.edge1)
        #set current to next and clear next set
        current = next
        next = set()

    return (nfa.accept in current)

infixes = ["a.b.c*", "a.(b|d).c*", "(a.(b|d))*","a.b(b.b)*.c"]
strings = ["", "abc","abbc", "abcc","abad", "abbbc"]

for i in infixes:
    for s in strings:
        print(match(i, s), i, s)