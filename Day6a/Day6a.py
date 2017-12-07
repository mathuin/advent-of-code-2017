#!/usr/bin/python3

import sys


# sixteen memory banks, banks can hold any number of blocks
# reallocation works in cycles
# for each cycle:
# - find bank with most blocks (ties won by lowest-numbered)
# - remove all blocks from that banks
# - add one to each bank after that one around and around
# - stop when allocation state repeats
# how many cycles?
def cycles(banks):
    blocks = [int(x) for x in banks.split()]
    history = []

    while True:
        history.append(list(blocks))
        k, v = [(k, v) for k, v in enumerate(blocks) if v == max(blocks)][0]
        togo = v
        blocks[k] = 0
        for j in range(0, togo):
            blocks[(k+j+1) % len(blocks)] += 1
        if blocks in history:
            break
    return len(history)

# Unit tests for cycles.
tt = {'0 2 7 0': 5}
for k, v in tt.items():
    result = cycles(k)
    if result != v:
        print("FAIL: input ", k, ": expected ", v, ", got ", result, sep="")

# The input is not checked for sanity, just existence.
banks = sys.stdin.readlines()
if len(banks) == 0:
    print("banks missing!")
    sys.exit(1)

# Only one line, and I don't want the newline character.
print(cycles(banks[0]))
