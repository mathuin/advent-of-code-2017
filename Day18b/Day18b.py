#!/usr/bin/python3

import sys

# duet

# assembly language
# snd X - transmit value to other program
# set X Y - assign register X with value Y
# add X Y - increase register X by value Y
# mul X Y - set reg X to reg X times value Y
# mod X Y - set reg X to reg X mod value Y
# rcv X - receive value from other program
# jgz X Y - jump with offset y if X is greater than 0
# how many times did program 1 send a value?


class Prog:
    def __init__(self, pid, insts):
        self.register = {'p': pid}
        self.insts = insts
        self.sent = 0
        self.outq = []
        self.inq = []
        self.pc = 0
        self.mode = "go"  # "block" and "stop" as well

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
        self.outq.append(self.val(x))
        self.sent += 1

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
        if not self.inq:
            self.mode = "block"
            return
        x = args[0]
        self.register[x] = self.inq.pop(0)

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
            self.mode = "stop"
        else:
            opcode, args = self.insts[self.pc]
            self.opcodes[opcode](self, args)
        if self.mode == "go":
            self.pc += 1


class Duet:
    def __init__(self, lines):
        insts = []
        for line in lines:
            args = line.rstrip().split()
            opcode = args.pop(0)
            insts.append((opcode, args))

        self.prog = [Prog(0, insts), Prog(1, insts)]
        self.stop = False

    def execute(self):
        if all(prog.mode == "block" for prog in self.prog):
            # deadlock
            self.stop = True
            return
        if all(prog.mode == "stop" for prog in self.prog):
            # all ended
            self.stop = True
        for i, prog in enumerate(self.prog):
            if prog.mode == "block":
                if prog.inq:
                    prog.mode = "go"
            if prog.mode == "go":
                prog.execute()
                if prog.outq:
                    self.prog[1-i].inq.append(prog.outq.pop(0))

    def onesent(self):
        return self.prog[1].sent


def work(lines):
    duet = Duet(lines)
    while not duet.stop:
        duet.execute()
        pass
    return duet.onesent()

# unit tests for work
tt = {
    'x': (
        [
            'snd 1\n',
            'snd 2\n',
            'snd p\n',
            'rcv a\n',
            'rcv b\n',
            'rcv c\n',
            'rcv d\n',
        ], 3)
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
