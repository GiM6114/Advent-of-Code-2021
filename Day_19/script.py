#
# Not really satisfied of this code efficiency/aesthically-wise, but really proud to have solved this pretty difficult challenge all by myself !
#


import numpy as np
from itertools import product
from math import ceil


# =============================================================================
# PART 1
# =============================================================================

#%%

data = open('input.txt','r').readlines()
probesPerScanner = []
currentScanner = []
for line in data[1:]:
    line = line[:-1]
    if not line:
        continue
    if 'scanner' in line:
        probesPerScanner.append(currentScanner.copy())
        currentScanner = []
        continue 
    coords = [int(i) for i in line.split(',')]
    currentScanner.append(coords)
probesPerScanner.append(currentScanner)    
n = len(probesPerScanner)

RMX = np.stack(
    [
        np.array([[1,0,0],[0,1,0],[0,0,1]],dtype='int16'), # 0°
        np.array([[1,0,0],[0,0,-1],[0,1,0]],dtype='int16'), # 90°
        np.array([[1,0,0],[0,-1,0],[0,0,-1]],dtype='int16'), # 180°
        np.array([[1,0,0],[0,0,1],[0,-1,0]],dtype='int16') # 270°
    ],axis = 2)

RMY = np.stack(
    [
        np.array([[1,0,0],[0,1,0],[0,0,1]],dtype='int16'), # 0°
        np.array([[0,0,1],[0,1,0],[-1,0,0]],dtype='int16'), # 90°
        np.array([[-1,0,0],[0,1,0],[0,0,-1]],dtype='int16'), # 180°
        np.array([[0,0,-1],[0,1,0],[1,0,0]],dtype='int16') # 270°
    ],axis = 2)

RMZ = np.stack(
    [
        np.array([[1,0,0],[0,1,0],[0,0,1]],dtype='int16'), # 0°
        np.array([[0,-1,0],[1,0,0],[0,0,1]],dtype='int16'), # 90°
        np.array([[-1,0,0],[0,-1,0],[0,0,1]],dtype='int16'), # 180°
        np.array([[0,1,0],[-1,0,0],[0,0,1]],dtype='int16') # 270°
    ],axis = 2)

prod_012 = list(product([0,1,2,3],repeat=3))

#%%
            
def findTransformationsToScanner(scanner,goalScanner,relativeTransformations, toAvoid=[]):
    print('searching transformation from',scanner,'to',goalScanner)
    for i,line in enumerate(relativeTransformations):
        if i in toAvoid:
            continue
        if line[scanner]:
            if i == 0:
                return [line[scanner]]
            temp = findTransformationsToScanner(i, goalScanner, relativeTransformations, toAvoid+[scanner])
            if temp:
                return [line[scanner]] + temp

def invertTransform(transform):
    rotMat = np.transpose(transform[0])
    pos = -rotMat @ transform[1]
    return [rotMat,list(pos)]

def nbFittingPoints(s1,s2,s2pos,rotMat):
    nb = 0
    for p2 in s2:
        p2_r_s1 = rotMat @ p2 + s2pos
        if list(p2_r_s1) in s1:
            nb += 1

    return nb

def inferScanner2RelativePosition(p1,p2,rotMat):
    p2_r_s1 = rotMat @ p2
    s2pos = [p1[i] - p2_r_s1[i] for i in range(3)]
    return s2pos

def isOverlapping(s1,s2):
    global RMX,RMY,RMZ
    for p1 in s1:
        for p2 in s2:
            for perm in prod_012:
                rotMat = RMX[:,:,perm[0]] @ RMY[:,:,perm[1]] @ RMZ[:,:,perm[2]]
                
                s2pos = inferScanner2RelativePosition(p1, p2, rotMat)
                # Try applying this rotation and position to other probes
                nbOfFitting = nbFittingPoints(s1,s2,s2pos,rotMat)
                if nbOfFitting >= 12:
                    # Found overlapping points
                    return [rotMat,s2pos]
    return False

#%%

# Find for every scanner every overlapping with other scanners
relativeTransformationsHalf = [[None for j in range(n)] for i in range(n)]
for s_i,s1 in enumerate(probesPerScanner[:-1]):
    print('Checking overlaps for scanner',s_i)
    for s_j,s2 in enumerate(probesPerScanner[s_i+1:]):
        s_j = s_i+s_j+1
        is_overlapping = isOverlapping(s1,s2)
        if is_overlapping:
            relativeTransformationsHalf[s_i][s_j] = is_overlapping
            print(f'Overlapping found between {s_i} and {s_j}.')
            print(is_overlapping)

print('All overlappings and reversed transforms found !')

# We found transfo i -> j (i < j).
# We can infer transfo j -> i (p_j = Rijp_i + O_j => p_i = Rij^Tp_j - Rij^TO_j)

#%%

relativeTransformations = [[None for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        if relativeTransformationsHalf[i][j]:
            relativeTransformations[i][j] = relativeTransformationsHalf[i][j]
            relativeTransformations[j][i] = invertTransform(relativeTransformationsHalf[i][j])
            
          
# With these overlappings and transformations, infer for every scanner the transformations needed to express its points in s0
transformationsNecessary = [[[np.identity(3,dtype='int16'),[0,0,0]]]]
for s_i,s in enumerate(probesPerScanner[1:]):
    s_i += 1
    transfosNeeded = findTransformationsToScanner(s_i,0,relativeTransformations)
    transformationsNecessary.append(transfosNeeded)

pointsFromOrigin = set()
for i in range(n):
    probes = probesPerScanner[i]
    transfos = transformationsNecessary[i]
    probescan = []
    for probe in probes:
        for transfo in transfos:
            probe = transfo[0] @ probe + transfo[1]
        pointsFromOrigin.add(tuple(probe))
        probescan.append(tuple(probe))

pointsFromOrigin = sorted(pointsFromOrigin)
print('Nb of points :',len(pointsFromOrigin))   # 313

#%%

# =============================================================================
# PART 2
# =============================================================================

scannersPositions = [[0,0,0]] # relative to scanner 0
for i in range(1,n):
    transfos = transformationsNecessary[i]
    origin = np.array([0,0,0],dtype='int16')
    for transfo in transfos:
        print(transfo[1])
        origin = transfo[0]@origin + np.array(transfo[1],dtype='int16')
    scannersPositions.append(origin)
    print(i,origin)
 
def ManhattanDistance(p0,p1):
    return sum(map(lambda x,y : abs(x-y),p0,p1))

maxDistance = 0
for i in range(n):
    for j in range(n):
        distance = ManhattanDistance(scannersPositions[i],scannersPositions[j])
        if distance > maxDistance:
            maxDistance = distance
            
print('Highest Manhattan distance :',maxDistance)
