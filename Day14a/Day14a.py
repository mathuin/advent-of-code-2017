#!/usr/bin/python3

import sys
from collections import Counter

# disk defragmentation

# disk consists of 128x128 grid
# each row corresponds to knot hash output of key-rownum
# ex: if key flqrgnkx row 0, knot hash input is flqrgnkx-0
# hash output is 32 hex digits, or 128 binary digits
# if bit == 1, square is used
# return how many squares are used in total grid


# from Day10b
def denseHash(knotme):
    hashout = ''
    for block in range(0, 16):
        out = 0
        for elem in range (0, 16):
            out ^= knotme[block*16+elem]
        hashout += hex(out//16)[2:]
        hashout += hex(out%16)[2:]
    return hashout


def sparseHash(lengthstr):
    listsize = 256
    lengths = [ord(x) for x in list(lengthstr.rstrip())]
    lengths.extend([17,31,73,47,23])
    knotme = list(range(0, listsize))
    currpos = 0
    skip = 0

    for round in range(0, 64):
        for length in lengths:
            shortlist = knotme[currpos:currpos+length]
            if len(shortlist) < length:
                shortlist.extend(knotme[0:(currpos+length) % listsize])
            shortlist.reverse()
            for index, elem in enumerate(shortlist):
                knotme[(currpos+index) % listsize] = elem
            currpos = (currpos + length + skip) % listsize
            skip += 1
    return knotme


def countOnes(hexnum):
    binstr = "{0:b}".format(int(hexnum, 16))
    freq = Counter(binstr)
    return freq['1']


def work(key):
    result = 0
    for i in range(0, 128):
        hashin = "{0}-{1}".format(key, i)
        sparse = sparseHash(hashin)
        dense = denseHash(sparse)
        result += countOnes(dense)
    return result

# Unit tests for knotHash.
tt = {
    'flqrgnkx': 8108,
}
for k, v in tt.items():
    result = work(k)
    if result != v:
        print("FAIL: input ", k, ": expected ", v, ", got ", result, sep="")

# The input is not checked for sanity, just existence.
lengths = sys.stdin.readlines()
if len(lengths) == 0:
    print("lengths missing!")
    sys.exit(1)

print(work(lengths[0].rstrip()))
