# 4th day of Advent of Code 2022
# Matteo Martinelli

from pathlib import Path
import numpy as np
file_in = Path('input') / 'day4.txt'

ranges_couple = file_in.open().read().splitlines()
ranges = [(r.split(',')[0], r.split(',')[1]) for r in ranges_couple]

# Part 1
def check_total_overlapping(r1: str, r2: str) -> bool:
    r1_min, r1_max = (int(x) for x in r1.split('-'))
    r2_min, r2_max = (int(x) for x in r2.split('-'))
    
    return ((r1_min <= r2_min) & (r1_max >= r2_max)) or ((r1_min >= r2_min) & (r1_max <= r2_max))

a = [check_total_overlapping(r[0], r[1]) for r in ranges]
print(sum(a))

# Part 2
def check_partial_overlapping(r1: str, r2: str) -> bool:
    r1_min, r1_max = (int(x) for x in r1.split('-'))
    r2_min, r2_max = (int(x) for x in r2.split('-'))
    return (r1_min in range(r2_min, r2_max+1) or r1_max in range(r2_min, r2_max+1)) or (r2_min in range(r1_min, r1_max+1) or r2_max in range(r1_min, r1_max+1))

a = [check_partial_overlapping(r[0], r[1]) for r in ranges]
print(sum(a))
