# 3rd day of Advent of Code 2022
# Matteo Martinelli

from pathlib import Path
import numpy as np
file_in = Path('input') / 'day3.txt'

def get_priority(item: str) -> int:
    return ord(item)-38 if item.isupper() else ord(item)-96

# Part 1
rucksacks = file_in.open().read().splitlines()
priority = 0

for r in rucksacks:
    for i in r[:int(len(r)/2)]:
        if i in r[int(len(r)/2):]:
            priority += get_priority(i)
            break
print(priority)

# Part 2
badges_priority = 0
for s in range(0, int(len(rucksacks)), 3):
    for i in rucksacks[s]:
        if i in rucksacks[s+1] and i in rucksacks[s+2]:
            badges_priority+=get_priority(i)
            break

print(badges_priority)
