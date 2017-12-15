#!/usr/bin/python3

import sys

# dueling generators

# two generators, A and B
# same algorithm: take prev value, multiply by factor,
# divide by 2147483647, keep remainder
# generator A uses factor of 16807, B uses 48271
# example: A starts with 65 and B starts with 8921
# if lowest 16 bits of both values match, increment total


def gen(prev, factor):
    return prev * factor % 2147483647


def genA(prev):
    return gen(prev, 16807)


def genB(prev):
    return gen(prev, 48271)


def judge(a, b):
    return a % 65536 == b % 65536


def work(lines, iters):
    hits = 0
    valueA = int(lines[0].split()[4])
    valueB = int(lines[1].split()[4])
    for i in range(0, iters):
        nvA = genA(valueA)
        nvB = genB(valueB)
        if judge(nvA, nvB):
            hits += 1
        valueA = nvA
        valueB = nvB
    return hits

# Unit tests for knotHash.
tt = {
    'x': (['Generator A starts with 65\n', 'Generator B starts with 8921\n'], 5, 1),
}
for k, v in tt.items():
    result = work(v[0], v[1])
    if result != v[2]:
        print("FAIL: input ", v[0], v[1], ": expected ", v[2], ", got ", result, sep="")

# The input is not checked for sanity, just existence.
lines = sys.stdin.readlines()
if len(lines) == 0:
    print("lines missing!")
    sys.exit(1)

print(work(lines, 40000000))
