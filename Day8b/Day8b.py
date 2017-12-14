#!/usr/bin/python3

import sys

# I heard you like registers

# instructions have parts:
# - register to modify
# - whether to increase or decrease
# - amount to change by
# - 'if'
# - register to check
# - comparison operator
# - amount to compare against
# 'b inc 5 if a > 1' - check a, if greater than 1, add 5 to b


def getValue(registers, name):
    if name not in registers:
        registers[name] = 0
    return registers[name]


def setValue(registers, name, value):
    registers[name] = value


def addValue(registers, name, value):
    setValue(registers, name, getValue(registers, name) + value)


def subValue(registers, name, value):
    setValue(registers, name, getValue(registers, name) - value)


dirCase = {
    'inc': addValue,
    'dec': subValue,
}


def greaterThan(registers, a, b):
    return getValue(registers, a) > b


def lessThan(registers, a, b):
    return getValue(registers, a) < b


def equalTo(registers, a, b):
    return getValue(registers, a) == b


def greaterThanEqualTo(registers, a, b):
    return not lessThan(registers, a, b)


def lessThanEqualTo(registers, a, b):
    return not greaterThan(registers, a, b)


def notEqualTo(registers, a, b):
    return not equalTo(registers, a, b)

opCase = {
    '>': greaterThan,
    '<': lessThan,
    '==': equalTo,
    '>=': greaterThanEqualTo,
    '<=': lessThanEqualTo,
    '!=': notEqualTo,
}


# what is the largest amount in any register at any time?
def largestValue(instructions):
    registers = {}

    value = "lame"
    for instruction in instructions:
        target, dir, mag, ifword, check, op, comp = instruction.split()
        if opCase[op](registers, check, int(comp)):
            dirCase[dir](registers, target, int(mag))
            if value == "lame" or getValue(registers, target) > value:
                value = getValue(registers, target)

    return value


# Unit tests for largestValue.
tt = {'x': (['b inc 5 if a > 1', 'a inc 1 if b < 5', 'c dec -10 if a >= 1', 'c inc -20 if c == 10'], 10)}
for k, v in tt.items():
    result = largestValue(v[0])
    if result != v[1]:
        print("FAIL: input ", v[0], ": expected ", v[1], ", got ", result, sep="")

# The input is not checked for sanity, just existence.
instructions = sys.stdin.readlines()
if len(instructions) == 0:
    print("instructions missing!")
    sys.exit(1)

print(largestValue(instructions))
