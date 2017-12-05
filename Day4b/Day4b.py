#!/usr/bin/python3

import sys


# For added security, yet another system policy has been put in place. Now, a
# valid passphrase must contain no two words that are anagrams of each other
# - that is, a passphrase is invalid if any word's letters can be rearranged
# to form any other word in the passphrase.
#
# For example:
#
#  - abcde fghij is a valid passphrase.
#  - abcde xyz ecdab is not valid - the letters from the third word can be
#    rearranged to form the first word.
#  - a ab abc abd abf abj is a valid passphrase, because all letters need
#    to be used when forming another word.
#  - iiii oiii ooii oooi oooo is valid.
#  - oiii ioii iioi iiio is not valid - any of these words can be
#    rearranged to form any other word.
#
# Under this new system policy, how many passphrases are valid?
def countValid(passphrases):
    valid = 0
    for passphrase in passphrases:
        words = passphrase.split()
        sets = []
        notValid = 0
        for word in words:
            letters = sorted(list(word))
            if letters in sets:
                notValid = 1
                break
            sets.append(letters)
        if notValid == 0:
            valid += 1
    return valid


# Unit tests for countValid.
tt = {'x': (['abcde fghij\n', 'abcde xyz ecdab\n', 'a ab abc abd abf abj\n', 'iiii oiii ooii oooi oooo\n', 'oiii ioii iioi iiio\n'], 3)}
for k, v in tt.items():
    result = countValid(v[0])
    if result != v[1]:
        print("FAIL: input ", v[0], ": expected ", v[1], ", got ", result, sep="")


# The input is not checked for sanity, just existence.
passphrases = sys.stdin.readlines()
if len(passphrases) == 0:
    print("passphrases missing!")
    sys.exit(1)

# Only one line, and I don't want the newline character.
print(countValid(passphrases))
