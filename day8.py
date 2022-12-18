# 8th day of Advent of Code 2022
# Matteo Martinelli

from pathlib import Path
import numpy as np
from enum import Enum
from typing import Tuple

class Directions(Enum):
    LEFT = (0, -1)
    RIGHT = (0, 1)
    TOP = (-1, 0)
    DOWN = (1, 0)

    def __add__(self, other: Tuple[int, int]):
        return tuple(sum(tup) for tup in zip(self.value, other))


file_in = Path('input') / 'day8.txt'

# pre-process
trees = file_in.open().read().splitlines()
trees = np.array([list(r) for r in trees])

# Part 1
intern_visible = 0
for i in range(1, trees.shape[0]-1):
    for j in range(1, trees.shape[1]-1):
        tree = trees[i, j]
        row = trees[i, :]
        col = trees[:, j]

        top = col[:i] < tree
        left = row[:j] < tree
        right = row[j+1:] < tree
        down = col[i+1:] < tree
        visible = top.all() | down.all() | left.all() |right.all()
        intern_visible += 1 if visible else 0

tot_visible = intern_visible + 2*(trees.shape[0]+trees.shape[1]-2)
print('Visible trees: ', tot_visible)

# Part 2
def is_position_ok(trees: np.array, pos: Tuple[int, int]) -> bool:
    max_row = trees.shape[0]
    max_col = trees.shape[1]
    return (0 <= pos[0] < max_row) and (0 <= pos[1] < max_col)

def scenic_score(trees: np.array, dir: Directions, pos: Tuple[int, int]) -> int:
    tree = float(trees[pos])
    pos = dir + pos 
    if not is_position_ok(trees, pos):
        return 0
    else:
        height = trees[pos] 
    score = 1
    while float(height) < tree:
        pos = dir + pos
        if is_position_ok(trees, pos):
            height = trees[pos]
        else:
            break
        score +=1
    return score 



    return score
scenic_scores = []
debug = dict()
for i in range(1, trees.shape[0]-1):
    for j in range(1, trees.shape[1]-1):
        scenic_scores.append(
            scenic_score(trees, Directions.TOP, (i, j)) *
            scenic_score(trees, Directions.LEFT, (i, j)) *
            scenic_score(trees, Directions.RIGHT, (i, j)) *
            scenic_score(trees, Directions.DOWN, (i, j))

        )

print(max(scenic_scores))
    