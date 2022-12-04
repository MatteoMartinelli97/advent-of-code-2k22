# 4th day of Advent of Code 2022
# Matteo Martinelli

from pathlib import Path
import numpy as np
file_in = Path('input') / 'day4.txt'

ranges_couple = file_in.open().read().splitlines()
ranges = [r.split(',') for r in ranges_couple]

# Part 1
def is_total_overlap(r1: str, r2: str) -> bool:
    r1_min, r1_max = (int(x) for x in r1.split('-'))
    r2_min, r2_max = (int(x) for x in r2.split('-'))
    
    return ((r1_min <= r2_min) & (r1_max >= r2_max)) or ((r1_min >= r2_min) & (r1_max <= r2_max))

total_overlap = [is_total_overlap(r[0], r[1]) for r in ranges]
print(sum(total_overlap))

# Part 2
def is_partial_overlap(r1: str, r2: str) -> bool:
    r1_min, r1_max = (int(x) for x in r1.split('-'))
    r2_min, r2_max = (int(x) for x in r2.split('-'))
    return r2_min <= r1_min <= r2_max or r1_min <= r2_min <= r1_max 

partial_overlap = [is_partial_overlap(r[0], r[1]) for r in ranges]
print(sum(partial_overlap))
