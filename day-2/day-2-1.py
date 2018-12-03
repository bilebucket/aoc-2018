#! /usr/bin/env python3
from collections import Counter


def checksum(lines):
    twos = 0
    threes = 0
    for line in lines:
        twos_changed, threes_changed = False, False
        counter = Counter(line)
        for v in counter.values():
            if v == 3 and not threes_changed:
                threes += 1
                threes_changed = True
            if v == 2 and not twos_changed:
                twos += 1
                twos_changed = True

    return twos * threes


with open("input", 'r') as f:
    print(checksum(f.readlines()))
