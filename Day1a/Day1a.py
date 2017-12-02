#!/usr/bin/python3

import sys


# The captcha requires you to review a sequence of digits (your puzzle input)
# and find the sum of all digits that match the next digit in the list. The
# list is circular, so the digit after the last digit is the first digit in
# the list.
def captcha(seq):
    # Split sequence into individual digits.
    seql = [int(x) for x in seq]

    # Perform the operation on the list
    sum = 0
    last = len(seq)-1
    for i in range(len(seq)):
        v = seql[i]
        if v == seql[0 if (i == last) else (i+1)]:
            sum += v
    return sum

# Unit tests for captcha.
tt = {'1122': 3, '1111': 4, '1234': 0, '91212129': 9}
for k, v in tt.items():
    result = captcha(k)
    if result != v:
        print("FAIL: input ", k, ": expected ", v, ", got ", result, sep="")

# The input is not checked for sanity, just existence.
seq = sys.stdin.readlines()
if len(seq) == 0:
    print("Sequence missing!")
    sys.exit(1)

# Only one line, and I don't want the newline character.
print(captcha(seq[0][:-1]))
