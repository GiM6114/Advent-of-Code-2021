import re
import numpy as np

with open('input.txt','r') as f:
    data = f.readlines()

points = set()
folds = []
for line in data:
    line = line[:-1]
    if len(line) == 0:
        continue
    if line[0] != 'f':
        pointCoords = line.split(',')
        points.add((int(pointCoords[0]),int(pointCoords[1])))
    else:
        regex = r'fold along (x|y)=([0-9]+)'
        m = re.match(regex,line)
        folds.append((m.group(1),int(m.group(2))))

# =============================================================================
# PART 1
# =============================================================================

def applyFold(points,fold):
    dim,value = fold
    
    newPoints = set()
    if dim == 'x':   
        for point in points:
            if point[0] > value:
                newPoints.add((point[0]-2*(point[0]-value),point[1]))
            else:
                newPoints.add((point[0],point[1]))
    else:
        for point in points:
            if point[1] > value:
                newPoints.add((point[0],point[1]-2*(point[1]-value)))
            else:
                newPoints.add((point[0],point[1]))  
    
    return newPoints
        

    
newPoints = applyFold(points,folds[0])
print(len(newPoints)) # 708

# =============================================================================
# PART 2
# =============================================================================

newPoints = points
for fold in folds:
    newPoints = applyFold(newPoints,fold)
    
xSize = max(map(lambda x: x[0],newPoints))+1
ySize = max(map(lambda x: x[1],newPoints))+1

array = np.zeros([xSize,ySize],dtype='bool')

for x,y in newPoints:
    array[x,y] = True

for j in range(ySize):
    for i in range(xSize):
        print('#' if array[i,j] else '.', end='')
    print('\n',end='')
    
# prints EBLUBRFH