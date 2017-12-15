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


def knotHash(listsize, lengthstr):
    lengths = [int(x) for x in lengthstr.split(',')]
    knotme = list(range(0, listsize))
    currpos = 0
    skip = 0

    for length in lengths:
        shortlist = knotme[currpos:currpos+length]
        if len(shortlist) < length:
            shortlist.extend(knotme[0:(currpos+length) % listsize])
        shortlist.reverse()
        for index, elem in enumerate(shortlist):
            knotme[(currpos+index) % listsize] = elem
        currpos = (currpos + length + skip) % listsize
        skip += 1

    return knotme[0]*knotme[1]


# Unit tests for knotHash.
tt = {'x': ((5, "3,4,1,5"), 12)}
for k, v in tt.items():
    result = knotHash(v[0][0], v[0][1])
    if result != v[1]:
        print("FAIL: input ", v[0], ": expected ", v[1], ", got ", result, sep="")

# The input is not checked for sanity, just existence.
lengths = sys.stdin.readlines()
if len(lengths) == 0:
    print("lengths missing!")
    sys.exit(1)

print(knotHash(256, lengths[0]))
