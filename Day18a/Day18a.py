#!/usr/bin/python3

import sys

# duet

# assembly language
# snd X - play sound with freq X
# set X Y - assign register X with value Y
# add X Y - increase register X by value Y
# mul X Y - set reg X to reg X times value Y
# mod X Y - set reg X to reg X mod value Y
# rcv X - recover freq last sound played when X not zero
# jgz X Y - jump with offset y if X is greater than 0
# what is value of recovered frequency first time rcv executes?


class Duet:
    def __init__(self, lines):
        self.lastfreq = -1
        self.pc = 0
        self.register = {}
        self.stop = False
        self.insts = []
        for line in lines:
            args = line.rstrip().split()
            opcode = args.pop(0)
            self.insts.append((opcode, args))

    def val(self, x):
        try:
            i = int(x)
            return i
        except ValueError:
            if x not in self.register:
                self.register[x] = 0
            return self.register[x]
        except Exception as e:
            print("Unexpected error {}".format(e))

    def snd(self, args):
        x = args[0]
        self.lastfreq = self.val(x)

    def set(self, args):
        x, y = args
        self.register[x] = self.val(y)

    def add(self, args):
        x, y = args
        self.register[x] = self.val(x) + self.val(y)

    def mul(self, args):
        x, y = args
        self.register[x] = self.val(x) * self.val(y)

    def mod(self, args):
        x, y = args
        self.register[x] = self.val(x) % self.val(y)

    def rcv(self, args):
        x = args[0]
        if self.val(x) == 0:
            # rcv is skipped when value of argument is zero
            return
        if self.lastfreq == -1:
            # rcv should not be called if snd has not been called
            print("snd not yet called!")
            return
        # stop on first successfuly rcv execution
        self.stop = True

    def jgz(self, args):
        x, y = args
        if self.val(x) > 0:
            # one short because execute() bumps by one
            self.pc += self.val(y)-1

    opcodes = {
        'snd': snd,
        'set': set,
        'add': add,
        'mul': mul,
        'mod': mod,
        'rcv': rcv,
        'jgz': jgz
    }

    def execute(self):
        if self.pc < 0 or self.pc > len(self.insts):
            print("PC out of bounds!")
            self.stop = True
        else:
            opcode, args = self.insts[self.pc]
            self.opcodes[opcode](self, args)
            self.pc += 1


def work(lines):
    duet = Duet(lines)
    while not duet.stop:
        duet.execute()
        pass
    return duet.lastfreq

# unit tests for work
tt = {
    'x': (
        [
            'set a 1\n',
            'add a 2\n',
            'mul a a\n',
            'mod a 5\n',
            'snd a\n',
            'set a 0\n',
            'rcv a\n',
            'jgz a -1\n',
            'set a 1\n',
            'jgz a -2\n',
        ], 4)
}
for k, v in tt.items():
    result = work(v[0])
    if result != v[1]:
        print("FAIL: input ", v[0], ": expected ", v[1], ", got ", result, sep="")

# The input is not checked for sanity, just existence.
lines = sys.stdin.readlines()
if len(lines) == 0:
    print("lines missing!")
    sys.exit(1)

print(work(lines))
