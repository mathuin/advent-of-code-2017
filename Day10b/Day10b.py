#!/usr/bin/python3

import sys

# knot hash

# start with:
# - a list of numbers 0-255
# - current position of 0
# - skip size of 0
# for each length in a sequence of lengths:
# - reverse order of that length in the list starting from current position
# - move the current position forward by that length plus skip size
# - increase skip size by one

# list is circular, if current position and length try to reverse elements beyond end of list, reverse from the front too.  if current position moves past end, wrap to front.
# lengths larger than list size are invalid.


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


# Unit tests for knotHash.
tt = {
    '': 'a2582a3a0e66e6e86e3812dcb672a272',
    'AoC 2017': '33efeb34ea91902bb2f59c9920caa6cd',
    '1,2,3': '3efbe78a8d82f29979031a4aa0b16a9d',
    '1,2,4': '63960835bcdc130f0b66d7ff4f6a5a8e',
}
for k, v in tt.items():
    sparse = sparseHash(k)
    result = denseHash(sparse)
    if result != v:
        print("FAIL: input ", k, ": expected ", v, ", got ", result, sep="")

# The input is not checked for sanity, just existence.
lengths = sys.stdin.readlines()
if len(lengths) == 0:
    print("lengths missing!")
    sys.exit(1)

sparse = sparseHash(lengths[0])
print(denseHash(sparse))
