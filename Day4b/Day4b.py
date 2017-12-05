#!/usr/bin/python3

import sys


# A new system policy has been put in place that requires all accounts to use
# a passphrase instead of simply a password. A passphrase consists of a
# series of words (lowercase letters) separated by spaces.
#
# To ensure security, a valid passphrase must contain no duplicate words.
#
# For example:
#
# aa bb cc dd ee is valid.
# aa bb cc dd aa is not valid - the word aa appears more than once.
# aa bb cc dd aaa is valid - aa and aaa count as different words.
# The system's full passphrase list is available as your puzzle input. How
# many passphrases are valid?
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

# The input is not checked for sanity, just existence.
passphrases = sys.stdin.readlines()
if len(passphrases) == 0:
    print("passphrases missing!")
    sys.exit(1)

# Only one line, and I don't want the newline character.
print(countValid(passphrases))
