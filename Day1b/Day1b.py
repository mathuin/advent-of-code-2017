#!/usr/bin/python3

import sys


# Now, instead of considering the next digit, it wants you to consider the
# digit halfway around the circular list. That is, if your list contains 10
# items, only include a digit in your sum if the digit 10/2 = 5 steps forward
# matches it. Fortunately, your list has an even number of elements.
def captcha(seq):
    # Split sequence into individual digits.
    seql = [int(x) for x in seq]

    # Perform the operation on the list
    sum = 0
    seqlen = len(seq)
    step = int(seqlen/2)
    for i in range(len(seq)):
        v = seql[i]
        if v == seql[(i+step) % seqlen]:
            sum += v
    return sum

# Unit tests for captcha.
tt = {'1212': 6, '1221': 0, '123425': 4, '123123': 12, '12131415': 4}
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
