#!/usr/bin/python3

import sys

# coprocessor conflagration

# assembly like day 18
# set x y sets register X to value of y
# sub x y decreases register x by value of y
# mul x y sets register x to value of multiplying value in register x by value of y
# jnz jumps with offset of value y only if value of x is not zero

# eight registers, a through h, all start at 0.

# how many times is the mul instruction invoked?


class Fire:
    def __init__(self, lines):
        self.register = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0}
        self.pc = 0
        self.stop = False
        self.mulcount = 0
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
                raise ValueError
            return self.register[x]
        except Exception as e:
            print("Unexpected error {}".format(e))

    def set(self, args):
        x, y = args
        self.register[x] = self.val(y)

    def sub(self, args):
        x, y = args
        self.register[x] = self.val(x) - self.val(y)

    def mul(self, args):
        x, y = args
        self.register[x] = self.val(x) * self.val(y)
        self.mulcount += 1

    def jnz(self, args):
        x, y = args
        if self.val(x) != 0:
            # one short because execute() bumps by one
            self.pc += self.val(y)-1

    opcodes = {
        'set': set,
        'sub': sub,
        'mul': mul,
        'jnz': jnz
    }

    def execute(self):
        if self.pc < 0 or self.pc >= len(self.insts):
            self.stop = True
        else:
            opcode, args = self.insts[self.pc]
            self.opcodes[opcode](self, args)
            self.pc += 1


def work(lines):
    fire = Fire(lines)
    print("program has ", len(fire.insts), " insts")
    while not fire.stop:
        fire.execute()
    return fire.mulcount

# The input is not checked for sanity, just existence.
lines = sys.stdin.readlines()
if len(lines) == 0:
    print("lines missing!")
    sys.exit(1)

print(work(lines))
