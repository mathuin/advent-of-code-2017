#!/usr/bin/python3

import sys
from math import sqrt

# coprocessor conflagration

# assembly like day 18
# set x y sets register X to value of y
# sub x y decreases register x by value of y
# mul x y sets register x to value of multiplying value in register x by value of y
# jnz jumps with offset of value y only if value of x is not zero

# eight registers, a through h, all start at 0.

# what value would be left in register h?

# help from DFreiberg on Reddit:
# https://www.reddit.com/r/adventofcode/comments/7lms6p/2017_day_23_solutions/drnjwq7/

# h is the number of composite numbers between the lower limit and upper limit, counting by 17.


def scanLines(lines):
    fire = Fire(lines)
    fire.insts = fire.insts[:8]
    while not fire.stop:
        fire.execute()
    return fire.register['b'], fire.register['c']


def isPrime(n):
    midpt = int(sqrt(n))
    for i in range(2, midpt):
        if n % i == 0:
            return False
    return True


def countH(lower, upper):
    regH = 0
    for i in range(lower, upper+17, 17):
        if not isPrime(i):
            regH += 1
    return regH


class Fire:
    def __init__(self, lines):
        self.register = {'a': 1, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0}
        self.pc = 0
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
    # fire = Fire(lines)
    # print("program has ", len(fire.insts), " insts")
    # while not fire.stop:
    #     fire.execute()
    lower, upper = scanLines(lines)
    return countH(lower, upper)

# The input is not checked for sanity, just existence.
lines = sys.stdin.readlines()
if len(lines) == 0:
    print("lines missing!")
    sys.exit(1)

print(work(lines))
