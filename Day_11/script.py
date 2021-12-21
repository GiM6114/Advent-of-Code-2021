import numpy as np

with open('input.txt', 'r') as f:
    data = np.genfromtxt(f,delimiter=1,dtype='uint8')
    
paddedData = np.ones([data.shape[0]+2,data.shape[1]+2])
paddedData[1:-1,1:-1] = data

def increment(i,j,alreadyFlashed,paddedData):
    if i < 1 or j < 1 or i > paddedData.shape[0]-2 or j > paddedData.shape[1]-2:
        return
    if alreadyFlashed[i,j]:
        return
    
    global nbFlashes
    
    if paddedData[i,j] == 9:
        alreadyFlashed[i,j] = True
        for x in range(-1,2):
            for y in range(-1,2):
                if x == 0 and y == 0:
                    continue
                increment(i+x,j+y,alreadyFlashed,paddedData)
        paddedData[i,j] = 0
        nbFlashes += 1
    else:
        paddedData[i,j] += 1

def simulateStep(paddedData):
    global allFlash
    alreadyFlashed = np.zeros(paddedData.shape,dtype='bool')
    for i in range(1,paddedData.shape[0]-1):
        for j in range(1,paddedData.shape[1]-1):
            increment(i,j,alreadyFlashed,paddedData)
            
    for i in range(1,paddedData.shape[0]-1):
        for j in range(1,paddedData.shape[1]-1):
            if paddedData[i,j] != 0:
                return
            
    allFlash = True

# =============================================================================
# PART 1 & PART 2 (lets do everything in one pass !)
# =============================================================================

nbSteps = 100
nbFlashes = 0
allFlash = False
k = 0
while not allFlash:
    simulateStep(paddedData)
    if k == 100:
        print(nbFlashes) # 1,620        
    k += 1
    
print(k) # 371
    
