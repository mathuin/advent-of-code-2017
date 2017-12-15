#!/usr/bin/python3

import sys

# packet scanners

# firewall consists of layers:
# depth: range

# packets traverse layers once per tick
# scanners traverse range one step per tick
# if scanner is at top of range when packets enter, packet is caught
# severity of trip is sum of depth*range for layers where packet is caught


def severity(layers):
    result = 0
    for layer in layers:
        depth, range = [int(x) for x in layer.rstrip().split(": ")]
        location = depth % ((range - 1) * 2)
        if location == 0:
            result += depth * range
    return result

# Unit tests for severity.
tt = {
    'x': (['0: 3\n', '1: 2\n', '4: 4\n', '6: 4\n'], 24)
}
for k, v in tt.items():
    result = severity(v[0])
    if result != v[1]:
        print("FAIL: input ", v[0], ": expected ", v[1], ", got ", result, sep="")

# The input is not checked for sanity, just existence.
layers = sys.stdin.readlines()
if len(layers) == 0:
    print("lines missing!")
    sys.exit(1)

print(severity(layers))
