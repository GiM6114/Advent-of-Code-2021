import numpy as np


with open('input.txt', 'r') as f:
    commandsTxt = f.read()

commands = commandsTxt.split('\n')[:-1]
commands = [str.split(c,' ') for c in commands]

# =============================================================================
# PART 1
# =============================================================================

horizontalPos = 0
depth = 0

for command in commands:
    nature = command[0]
    value = int(command[1])
    if nature == 'forward':
        horizontalPos += value
    elif nature == 'down':
        depth += value
    elif nature == 'up':
        depth -= value

print(horizontalPos*depth) # 1,962,940

# =============================================================================
# PART 2
# =============================================================================

horizontalPos = 0
depth = 0
aim = 0
for command in commands:
    nature = command[0]
    value = int(command[1])
    if nature == 'forward':
        horizontalPos += value
        depth += aim * value
    elif nature == 'down':
        aim += value
    elif nature == 'up':
        aim -= value

print(horizontalPos*depth) # 1,813,664,422