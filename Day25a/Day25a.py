#!/usr/bin/python3

import sys
from re import match, MULTILINE

# halting problem

# process Turing machine as specified
# in state X:
# if value is Y:
# write the value Z
# move either left or right
# change to state W
# return number of 1's


def findit(regexp, line):
    m = match(regexp, line, MULTILINE)
    if m:
        return m.groups()
    return None


class Turing:
    def __init__(self, state, iters, states):
        self.tape = {}
        self.cursor = 0
        self.state = state
        self.iters = iters
        self.states = states

    def countones(self):
        return sum([value for key, value in self.tape.items()])


    # def __oldinit__(self, lines):
    #     self.tape = {}
    #     self.cursor = 0
    #     self.states = states
    #
    #
    #     self.state = findit(r'Begin in state ([A-Z]).', lines.pop(0))[0]
    #     print("self.state = ", self.state)
    #     self.iters = findit(r'Perform a diagnostic checksum after ([0-9]*) steps.', lines.pop(0))[0]
    #     print("self.iters = ", self.iters)
    #
    #     newstate = None
    #     while True:
    #         if newstate is None:
    #             line = lines.pop(0)
    #             if line == '\n':
    #                 line = lines.pop(0)
    #             newstate = findit(r'In state ([A-Z]):', lines.pop(0))[0]
    #             newvalues = {}
    #             if newstate is None:
    #                 print("panic new state")
    #         else:
    #             if lines[0] == '\n':
    #                 self.states[newstate] = newvalues
    #                 newstate = None
    #                 newvalues = {}
    #                 continue
    #             inval, outval, dir, nextstate = findit(r'  If the current value is ([0-1]):\n    - Write the value ([0-1]).\n    - Move one slot to the ([a-z]*).\n    - Continue with state ([A-Z]).', ''.join(lines[:3]))[:3]
    #             print(inval, outval, dir, nextstate)
    #             if inval and outval and dir and nextstate:
    #                 newvalues[inval] = [outval, dir, nextstate]
    #                 for i in range(0, 3):
    #                     lines.pop(0)

# Running it until the number of steps required to take the listed diagnostic checksum would result in the following tape configurations (with the cursor marked in square brackets):
#
# ... 0  0  0 [0] 0  0 ... (before any steps; about to run state A)
# ... 0  0  0  1 [0] 0 ... (after 1 step;     about to run state B)
# ... 0  0  0 [1] 1  0 ... (after 2 steps;    about to run state A)
# ... 0  0 [0] 0  1  0 ... (after 3 steps;    about to run state B)
# ... 0 [0] 1  0  1  0 ... (after 4 steps;    about to run state A)
# ... 0  1 [1] 0  1  0 ... (after 5 steps;    about to run state B)
# ... 0  1  1 [0] 1  0 ... (after 6 steps;    about to run state A)
    def execute(self):
        currstate = self.states[str(self.state)]
        if self.cursor not in self.tape:
            self.tape[self.cursor] = 0
        under = self.tape[self.cursor]
        write, move, nextstate = currstate[under]
        self.tape[self.cursor] = write
        self.cursor += move
        self.state = nextstate


def work(state, iters, states):
    turing = Turing(state, iters, states)
    for i in range(0, turing.iters):
        turing.execute()
    return(turing.countones())


# Test case for work.
# tt = {'x': (['Begin in state A.\n', 'Perform a diagnostic checksum after 6 steps.\n', '\n', 'In state A:\n', '  If the current value is 0:\n', '    - Write the value 1.\n', '    - Move one slot to the right.\n', '    - Continue with state B.\n', '  If the current value is 1:\n', '    - Write the value 0.\n', '    - Move one slot to the left.\n', '    - Continue with state B.\n', '\n', 'In state B:\n', '  If the current value is 0:\n', '    - Write the value 1.\n', '  - Move one slot to the left.\n', '    - Continue with state A.\n', '  If the current value is 1:\n', '    - Write the value 1.\n', '    - Move one slot to the right.\n', '    - Continue with state A.\n'], 3)}
tt = {'x': ('A', 6, {'A': [[1, +1, 'B'], [0, -1, 'B']], 'B': [[1, -1, 'A'], [1, +1, 'A']]}, 3)}

for k, v in tt.items():
    result = work(v[0], v[1], v[2])
    if result != v[3]:
        print("FAIL: input ", v[0], ": expected ", v[3], ", got ", result, sep="")

# The input is not checked for sanity, just existence.
lines = sys.stdin.readlines()
if len(lines) == 0:
    print("lines missing!")
    sys.exit(1)

state = 'A'
iters = 12173597
states = {
    'A': [[1, +1, 'B'], [0, -1, 'C']],
    'B': [[1, -1, 'A'], [1, +1, 'D']],
    'C': [[1, +1, 'A'], [0, -1, 'E']],
    'D': [[1, +1, 'A'], [0, +1, 'B']],
    'E': [[1, -1, 'F'], [1, -1, 'C']],
    'F': [[1, +1, 'D'], [1, +1, 'A']],
}

print(work(state, iters, states))
