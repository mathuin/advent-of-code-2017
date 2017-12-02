#!/usr/bin/python3

import sys


# The spreadsheet consists of rows of apparently-random numbers. To make sure
# the recovery process is on the right track, they need you to calculate the
# spreadsheet's checksum. For each row, determine the difference between the
# largest value and the smallest value; the checksum is the sum of all of
# these differences.
def checksum(sheet):
    sum = 0
    for line in sheet:
        cells = [int(x) for x in line.split()]
        sum += max(cells)
        sum -= min(cells)
    return sum

tt = {'x': (['5 1 9 5\n', '7 5 3\n', '2 4 6 8\n'], 18)}
for k, v in tt.items():
    sheet = v[0]
    expected = int(v[1])
    result = checksum(sheet)
    if result != expected:
        print("FAIL: input ", sheet,
              ": expected ", expected,
              ", got ", result, sep="")

# Read spreadsheet from stdin.
sheet = sys.stdin.readlines()
if len(sheet) == 0:
    print("Spreadsheet must have at least one line!")
    sys.exit(1)

print(checksum(sheet))
