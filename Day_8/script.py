from itertools import permutations

with open('input.txt', 'r') as f:
    entries = f.readlines()

signalsOutputsList  = []
for entry in entries:
    signalOutput = entry.split(' | ')
    signals = signalOutput[0].split(' ')
    outputs = signalOutput[1][:-1].split(' ')
    signalsOutputsList.append((signals,outputs))

# =============================================================================
# PART 1
# =============================================================================

nbDigitsOfSize = [0]*10

for signals,outputs in signalsOutputsList:
    for output in outputs:
        nbDigitsOfSize[len(output)] += 1
        
nb1 = nbDigitsOfSize[2]
nb4 = nbDigitsOfSize[4]
nb7 = nbDigitsOfSize[3]
nb8 = nbDigitsOfSize[7]

print(nb1+nb4+nb7+nb8) # 521

# =============================================================================
# PART 2
# =============================================================================

                