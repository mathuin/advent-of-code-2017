#!/usr/bin/python3

import sys

# stream processing

# streams have groups and garbage.
# groups are delimited by {}.
# groups can contain other groups and garbage.
# garbage is delimited by <>.
# garbage can't contain groups.
# any character followed by ! is cancelled.
# goal is to find total score for all groups.
# group score = 1 + score of containing group.


# step one, remove all the !. from the stream.
def cancelChars(chars):
    for k, v in enumerate(chars):
        if v == '':
            continue
        if v == '!':
            chars[k] = ''
            chars[k+1] = ''
    return chars


# step two, remove all the <[^>]> from the stream.
def removeGarbage(chars):
    trash = False

    for k, v in enumerate(chars):
        if not trash and v == '<':
            trash = True
        if trash:
            chars[k] = ''
        if trash and v == '>':
            trash = False
    return chars


def countGroups(chars):
    groups = []
    depth = 0
    for k, v in enumerate(chars):
        if v == '{':
            depth += 1
        if v == '}':
            groups.append(depth)
            depth -= 1

    return sum(groups)

# Unit tests for countGroups
tt = {
    'a': ('{}', 1),
    'b': ('{{{}}}', 6),
    'c': ('{{},{}}', 5),
    'd': ('{{{},{},{{}}}}', 16),
    'e': ('{<a>,<a>,<a>,<a>}', 1),
    'f': ('{{<ab>},{<ab>},{<ab>},{<ab>}}', 9),
    'g': ('{{<!!>},{<!!>},{<!!>},{<!!>}}', 9),
    'h': ('{{<a!>},{<a!>},{<a!>},{<ab>}}', 3),
}
for k, v in tt.items():
    chars = list(v[0])
    chars = cancelChars(chars)
    chars = removeGarbage(chars)
    result = countGroups(chars)
    if result != v[1]:
        print("FAIL: input ", v[0], ": expected ", v[1], ", got ", result, sep="")

# The input is not checked for sanity, just existence.
stream = sys.stdin.readlines()
if len(stream) == 0:
    print("stream missing!")
    sys.exit(1)

chars = list(stream[0])
chars = cancelChars(chars)
chars = removeGarbage(chars)
print(countGroups(chars))
