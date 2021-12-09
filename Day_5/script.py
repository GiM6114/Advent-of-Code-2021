import numpy as np

with open('input.txt', 'r') as f:
    regex = r'([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)'
    data = np.fromregex(f,regex,dtype='int32')

# =============================================================================
# PART 1
# =============================================================================
    
crosses = {}
counter = 0
for row in data:
    
    x1,y1,x2,y2 = row[0],row[1],row[2],row[3]
    
    step = 1
    if x1 == x2: 
        if y1 > y2:
            step = -1
        for y in range(y1,y2+step,step):
            crosses[(x1,y)] = crosses.get((x1,y),0) + 1
            if crosses[(x1,y)] == 2:
                counter += 1
            
    elif y1 == y2:
        if x1 > x2:
            step = -1
        for x in range(x1,x2+step,step):
            crosses[(x,y1)] = crosses.get((x,y1),0) + 1
            if crosses[(x,y1)] == 2:
                counter += 1
            
            
print(counter) # 5,084

# =============================================================================
# PART 2
# =============================================================================
        
crosses = {}
counter = 0
for row in data:
    
    x1,y1,x2,y2 = row[0],row[1],row[2],row[3]
    
    step = 1
    if x1 == x2: 
        if y1 > y2:
            step = -1
        for y in range(y1,y2+step,step):
            crosses[(x1,y)] = crosses.get((x1,y),0) + 1
            if crosses[(x1,y)] == 2:
                counter += 1
            
    elif y1 == y2:
        if x1 > x2:
            step = -1
        for x in range(x1,x2+step,step):
            crosses[(x,y1)] = crosses.get((x,y1),0) + 1
            if crosses[(x,y1)] == 2:
                counter += 1
    
    else:
        stepX = 1
        stepY = 1
        if x1 > x2:
            stepX = -1
        if y1 > y2:
            stepY = -1
        for i in range(0,abs(x1-x2)+1):
            tempX = x1+stepX*i
            tempY = y1+stepY*i
            crosses[(tempX,tempY)] = crosses.get((tempX,tempY),0) + 1
            if crosses[(tempX,tempY)] == 2:
                counter += 1 
            
print(counter) # 17,882
