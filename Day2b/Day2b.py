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
        for i, elem in enumerate(cells):
            for oelem in cells[i+1:]:
                if elem > oelem:
                    if elem % oelem == 0:
                        sum += int(elem/oelem)
                else:
                    if oelem % elem == 0:
                        sum += int(oelem/elem)
    return sum

tt = {'x': (['5 9 2 8\n', '9 4 7 3\n', '3 8 6 5\n'], 9)}
for k, v in tt.items():
    sheet = v[0]
    expected = int(v[1])
    result = checksum(sheet)
    if result != expected:
        print("FAIL: input ", sheet,
              ": expected ", expected,
              ", got ", result, sep="")

# Read spreadsheet from file.
f = open('input', 'r')
sheet = f.readlines()
if len(sheet) == 0:
    print("Spreadsheet must have at least one line!")
    sys.exit(1)

print(checksum(sheet))
