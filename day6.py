# 6th day of Advent of Code 2022
# Matteo Martinelli

from pathlib import Path

file_in = Path('input') / 'day6.txt'

# pre-process
datastream = file_in.open().read()

# Part 1
for i in range(len(datastream)):
    if len(set(datastream[i:i+4])) == 4:
        print(i+4)
        break

# Part 2
for i in range(len(datastream)):
    if len(set(datastream[i:i+14])) == 14:
        print(i+14)
        break