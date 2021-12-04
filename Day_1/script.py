import numpy as np

with open('input.txt', 'r') as f:
    depths = f.read()

depths = np.fromstring(depths, dtype='uint16', sep='\n')

# =============================================================================
# PART 1
# =============================================================================

count = 0  
for idx, depth in enumerate(depths[1:]):
    if depth > depths[idx]:
        count += 1
        
print(count)

# =============================================================================
# PART 2
# =============================================================================

count = 0
previousSum = sum(depths[0:3])
for i in range(len(depths[1:-1])):
    currentSum = sum(depths[i:i+3])
    if currentSum > previousSum:
        count += 1
    previousSum = currentSum

print(count)