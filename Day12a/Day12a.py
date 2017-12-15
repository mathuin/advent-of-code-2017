#!/usr/bin/python3

import sys

# digital plumber

# list of ids
# id <-> ids-it-can-talk-with
# the latter is a comma delimited list


def makeIDs(lines):
    ids = {}
    for line in lines:
        id, op, linked = line.split(' ', 2)
        ids[id] = linked.replace(',', ' ').split()
    return ids


# how many ids are in the group that contains 0
def countIDs(ids, root):
    tocheck = [root]
    ingroup = [root]

    while tocheck:
        for id in tocheck:
            tocheck.remove(id)
            for newid in ids[id]:
                if newid not in ingroup:
                    ingroup.append(newid)
                    if newid not in tocheck:
                        tocheck.append(newid)
    return len(ingroup)

# Unit Tests for countIDs.
tt = {
    'x': (
            [
                '0 <-> 2\n',
                '1 <-> 1\n',
                '2 <-> 0, 3, 4\n',
                '3 <-> 2, 4\n',
                '4 <-> 2, 3, 6\n',
                '5 <-> 6\n',
                '6 <-> 4, 5\n',
            ],
            6
        )
}
for k, v in tt.items():
    ids = makeIDs(v[0])
    result = countIDs(ids, '0')
    if result != v[1]:
        print("FAIL: input ", v[0], ": expected ", v[1], ", got ", result, sep="")

# The input is not checked for sanity, just existence.
lines = sys.stdin.readlines()
if len(lines) == 0:
    print("lines missing!")
    sys.exit(1)

ids = makeIDs(lines)
print(countIDs(ids, '0'))
