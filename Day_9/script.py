import numpy as np

with open('input.txt', 'r') as f:
    data = np.genfromtxt(f,delimiter=1,dtype='uint8')

paddedData = np.multiply(np.ones([data.shape[0]+2,data.shape[1]+2],dtype='uint8'),10)
paddedData[1:-1,1:-1] = data

# =============================================================================
# PART 1
# =============================================================================

def isLowPoint(i,j,data):    
    return data[i,j]<data[i-1,j] and data[i,j]<data[i+1,j] and data[i,j]<data[i,j-1] and data[i,j]<data[i,j+1]

risk = 0
for i in range(1,paddedData.shape[0]-1):
    for j in range(1,paddedData.shape[1]-1):
        if isLowPoint(i,j,paddedData):
            risk += paddedData[i,j]+1
            
print(risk) # 591

# =============================================================================
# PART 2
# =============================================================================

def sumClosestLowest(i,j,data,marked):
    
    if (i,j) in marked:
        return 0
    marked[(i,j)] = True

    if data[i,j] in [9,10]:
        return 0
    
    _sum = 0
    if i > 0 and data[i-1,j] > data[i,j]:
        _sum += sumClosestLowest(i-1, j, data, marked)
    if i < data.shape[0]-1 and data[i+1,j] > data[i,j]:
        _sum += sumClosestLowest(i+1, j, data, marked)
    if j > 0 and data[i,j-1] > data[i,j]:
        _sum += sumClosestLowest(i, j-1, data, marked)
    if j < data.shape[1]-1 and data[i,j+1] > data[i,j]:
        _sum += sumClosestLowest(i, j+1, data, marked)
    return _sum + 1
    
def basinSizeFromLowPoint(i,j,data,marked):
    return sumClosestLowest(i,j,data,marked)

largestSizes = [0,0,0]
marked = {}

for i in range(1,paddedData.shape[0]-1):
    for j in range(1,paddedData.shape[1]-1):
        if isLowPoint(i,j,paddedData):
            basinSize = basinSizeFromLowPoint(i,j,paddedData,marked)
            largestSizes.append(basinSize)
            largestSizes.sort()
            largestSizes = largestSizes[1:4]
            
print(np.prod(largestSizes)) # 1,113,424
            