from collections import defaultdict

with open('input.txt','r') as f:
    data = f.readlines() 

def constructGraphFromData(data):
    
    graph = defaultdict(list)
    
    for line in data:
        line = line[:-1]
        nodeNames = line.split('-')
        graph[nodeNames[0]].append(nodeNames[1])
        graph[nodeNames[1]].append(nodeNames[0])

    return graph

def computeNbPaths(currentNode,path,graph,doubleUsed=True):
        
    if currentNode == 'end':
        return 1
    
    nbPaths = 0
    for nextNode in graph[currentNode]:
        if nextNode.isupper():
            nbPaths += computeNbPaths(nextNode,path+[nextNode],graph,doubleUsed)
        elif nextNode not in path:
            nbPaths += computeNbPaths(nextNode,path+[nextNode],graph,doubleUsed)
        elif not doubleUsed and nextNode != 'start':
            nbPaths += computeNbPaths(nextNode,path+[nextNode],graph,True)            
            
    return nbPaths

graph = constructGraphFromData(data)

# =============================================================================
# PART 1
# =============================================================================
        
nbPaths1 = computeNbPaths('start',['start'],graph)
print(nbPaths1) # 4,885

# =============================================================================
# PART 2
# =============================================================================
      
nbPaths2 = computeNbPaths('start',['start'],graph,False)
print(nbPaths2) # 117,095