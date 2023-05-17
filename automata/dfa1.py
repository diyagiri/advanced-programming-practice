from automata.fa.dfa import DFA

dfa=DFA(
    states={'q0','q1','q2','q3'},
    input_symbols={'0','1'},
    transitions={
        'q0':{'0':'q1','1':'q0'},
        'q1':{'0':'q2','1':'q0'},
        'q2':{'0':'q3','1':'q3'},
    },
    initial_state='q0',
    final_states={'q3'}
)
dfa.read_input('001')
dfa.read_input('011')
print(dfa.read_input_stepwise('011'))

if dfa.accepts_input('011'):
    print('accepted')
else:
    print('rejected')