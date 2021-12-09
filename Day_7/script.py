import numpy as np

with open('input.txt', 'r') as f:
    crabs = np.loadtxt(f,delimiter=',',dtype='uint32')

nbCrabs = len(crabs) 
mean = sum(crabs)//nbCrabs # used as a first approximation
maxCrab = max(crabs)

# =============================================================================
# PART 1
# =============================================================================

def getFuelNeeded(crabs,position):
    fuelNeeded = 0
    for crab in crabs:
        fuelNeeded += abs(crab - position)
    return fuelNeeded

minFuel = np.iinfo('uint32').max
for i in range(nbCrabs):
    fuelNeeded = getFuelNeeded(crabs,i)
    if fuelNeeded < minFuel:
        minFuel = fuelNeeded

print(minFuel) # 342,730

# =============================================================================
# PART 2
# =============================================================================

def getFuelNeeded2(crabs,position):
    fuelNeeded = 0
    for crab in crabs:
        fuelNeeded += sum(range(1,abs(crab - position)+1))
    return fuelNeeded

minFuel = np.iinfo('uint32').max
for i in range(nbCrabs):
    fuelNeeded = getFuelNeeded2(crabs,i)
    if fuelNeeded < minFuel:
        minFuel = fuelNeeded

print(minFuel) # 342,730