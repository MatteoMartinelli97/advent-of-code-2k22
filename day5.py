# 5th day of Advent of Code 2022
# Matteo Martinelli

from pathlib import Path
import re
import numpy as np
file_in = Path('input') / 'day5.txt'

def execute_instruction_CM9000 (inst: str, stacks : dict) -> dict:
    n, i_from, i_to = re.findall(r'\d+', inst)
    for _ in range(int(n)):
        b = stacks[int(i_from)].pop()
        stacks[int(i_to)].append(b)
    return stacks

def execute_instruction_CM9001 (inst: str, stacks : dict) -> dict:
    n, i_from, i_to = re.findall(r'\d+', inst)
    box_to_move = stacks[int(i_from)][-int(n):]
    stacks[int(i_from)] = stacks[int(i_from)][:-int(n)]
    stacks[int(i_to)] += box_to_move
    return stacks

# pre-process
crates, instructions = file_in.open().read().split('\n\n')
instructions = instructions.splitlines()
rows = crates.splitlines()
idxs = [int(i) for i in rows[-1].split()]
rows = rows[:-1]


# Part 1
stacks = {   i : [] for i in idxs}
for r in rows:
    for i, j in enumerate(range(0, len(r), 4)):
        box = r[j:j+3]
        if box.strip(' ') == '':
            continue
        else:
            box = box[1]
        stacks[idxs[i]].insert(0, box)

for instruction in instructions:
    stacks = execute_instruction_CM9000(instruction, stacks)
print(''.join([stacks[i][-1] for i in stacks.keys()]))

# Part 2
stacks = {   i : [] for i in idxs}
for r in rows:
    for i, j in enumerate(range(0, len(r), 4)):
        box = r[j:j+3]
        if box.strip(' ') == '':
            continue
        else:
            box = box[1]
        stacks[idxs[i]].insert(0, box)

for instruction in instructions:
    stacks = execute_instruction_CM9001(instruction, stacks)
print(''.join([stacks[i][-1] for i in stacks.keys()]))