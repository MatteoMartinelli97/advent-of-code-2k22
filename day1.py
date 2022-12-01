# 1st day of Advent of Code 2022
# Matteo Martinelli

from pathlib import Path
import numpy as np
file_in = Path('input') / 'day1.txt'

# Part 1 
calories = file_in.open().read().split('\n\n')
elf_calories = [sum([int(y) for y in x.splitlines()]) for x in calories ] 
print(max(elf_calories))

# Part 2
print(sum(np.sort(elf_calories)[-3:]))