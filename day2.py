# 2nd day of Advent of Code 2022
# Matteo Martinelli

from pathlib import Path
import numpy as np
from enum import Enum

class Shapes(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class Outcomes(Enum):
    LOSS = 0
    DRAW = 3
    WIN = 6

def outcome (s1: Shapes, s2: Shapes) -> int:
    if s1 == s2:
        return 3
    if s2 is Shapes.ROCK:
        return 0 if s1 is Shapes.PAPER else 6
    elif s2 is Shapes.PAPER:
        return 0 if s1 is Shapes.SCISSORS else 6
    else:
        return 0 if s1 is Shapes.ROCK else 6


first_player_map = {'A' : Shapes.ROCK, 'B' : Shapes.PAPER, 'C' : Shapes.SCISSORS}
second_player_map = {'X' : Shapes.ROCK, 'Y' : Shapes.PAPER, 'Z' : Shapes.SCISSORS}

file_in = Path('input') / 'day2.txt'

# Part 1
rounds = file_in.open().read().splitlines()
points = [ outcome( first_player_map[s.split(' ')[0]], 
                    second_player_map[s.split(' ')[1]]) + second_player_map[s.split(' ')[1]].value for s in rounds]
print(sum(points))

# Part 2
second_col_map = {'X' : Outcomes.LOSS, 'Y' : Outcomes.DRAW, 'Z' : Outcomes.WIN}

def what_to_play (s1: Shapes, r: Outcomes) -> Shapes:
    if r is Outcomes.DRAW:
        return s1
    if s1 is Shapes.ROCK:
        return Shapes.PAPER if r is Outcomes.WIN else Shapes.SCISSORS
    elif s1 is Shapes.PAPER:
        return Shapes.SCISSORS if r is Outcomes.WIN else Shapes.ROCK
    else:
        return Shapes.ROCK if r is Outcomes.WIN else Shapes.PAPER

points = [what_to_play( first_player_map[s.split(' ')[0]], 
                        second_col_map[s.split(' ')[1]]).value + second_col_map[s.split(' ')[1]].value for s in rounds]
print(sum(points))