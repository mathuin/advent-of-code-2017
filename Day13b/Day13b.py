#!/usr/bin/python3

import sys

# packet scanners

# firewall consists of layers:
# depth: range

# packets traverse layers once per tick
# scanners traverse range one step per tick
# if scanner is at top of range when packets enter, packet is caught
# severity of trip is sum of depth*range for layers where packet is caught
# how long can packet be delayed to avoid hitting any layers

def delay(layers):
    firewall = {}
    offset = 0
    for layer in layers:
        depth, range = [int(x) for x in layer.rstrip().split(": ")]
        firewall[depth] = range
    while True:
        caught = False
        for depth, range in firewall.items():
            location = (depth + offset) % ((range - 1) * 2)
            if location == 0:
                caught = True
                break
        if caught:
            offset += 1
        else:
            break
    return offset

# Unit tests for delay.
tt = {
    'x': (['0: 3\n', '1: 2\n', '4: 4\n', '6: 4\n'], 10)
}
for k, v in tt.items():
    result = delay(v[0])
    if result != v[1]:
        print("FAIL: input ", v[0], ": expected ", v[1], ", got ", result, sep="")

# The input is not checked for sanity, just existence.
layers = sys.stdin.readlines()
if len(layers) == 0:
    print("lines missing!")
    sys.exit(1)

print(delay(layers))
