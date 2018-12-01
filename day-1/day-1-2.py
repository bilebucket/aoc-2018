#! /usr/bin/env python3

from itertools import cycle

with open("./input", 'r') as f:
    numbers = [int(l) for l in f.readlines()]
    accum = 0
    seen = [accum]
    for number in cycle(numbers):
        accum += number
        if accum in seen:
            print(accum)
            break
        seen.append(accum)
