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
    return [x for x in chars if x != '']


# step two, remove all the <[^>]> from the stream.
def removeGarbage(chars):
    trash = False
    removed = 0

    for char in chars:
        if not trash and char == '<':
            trash = True
            removed -= 1
        if trash and char == '>':
            trash = False
        if trash:
            removed += 1
    return removed


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
    'a': ('<>', 0),
    'b': ('<random characters>', 17),
    'c': ('<<<<>', 3),
    'd': ('<{!>}>', 2),
    'e': ('<!!>', 0),
    'f': ('<!!!>>', 0),
    'g': ('<{o"i!a,<{i<a>', 10),
}
for k, v in tt.items():
    chars = list(v[0])
    chars = cancelChars(chars)
    result = removeGarbage(chars)
    if result != v[1]:
        print("FAIL: input ", v[0], ": expected ", v[1], ", got ", result, sep="")

# The input is not checked for sanity, just existence.
stream = sys.stdin.readlines()
if len(stream) == 0:
    print("stream missing!")
    sys.exit(1)

chars = list(stream[0])
chars = cancelChars(chars)
print(removeGarbage(chars))
