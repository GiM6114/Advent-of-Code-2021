import numpy as np

with open('input.txt', 'r') as f:
    reports = np.genfromtxt(f,dtype='uint8',delimiter=1)


# =============================================================================
# PART 1
# =============================================================================

nbLines = reports.shape[0]
halfNbLines = nbLines // 2
nbBits  = reports.shape[1]

gammaBinary = '0b'
for i in range(nbBits):
    nbOnes = np.sum(reports[:,i])
    gammaBinary += '1' if nbOnes > halfNbLines else '0'

gamma = int(gammaBinary,2)
epsilon = int('0b'+'1'*nbBits,2) - gamma

powerConsumption = gamma*epsilon
print(powerConsumption)

# =============================================================================
# PART 2
# =============================================================================

remainers = np.copy(reports)
for i in range(nbBits):
    nbOnes = sum(remainers[:,i])
    mostCommon = '1' if nbOnes > halfNbLines else '0'
    remainers = np.array()
