import numpy as np
from queue import PriorityQueue

with open('input.txt','r') as f:
    data = np.genfromtxt(f,delimiter=1,dtype='uint64')

# =============================================================================
# PART 1
# =============================================================================

# Let's do an A* algorithm

class Node:
    
    def __init__(self,pos,cost,heur,prevNode=None):
        self.pos = pos
        self.cost = cost
        self.heur = heur
        self.prevNode = prevNode
            
    def __gt__(self,other):
        return self.cost+self.heur > other.cost+other.heur


# Heuristic used here : L1 distance (= Manhattan distance)
def computeHeuristic(pos,end):
    x1,y1 = pos
    x2,y2 = end
    return abs(x1 - x2) + abs(y1 - y2)

def buildPath():
    pass

def adjacentPositions(node,size):
    x,y = node
    adjPos = []
    if x > 0:
        adjPos.append((x-1,y))
    if y > 0:
        adjPos.append((x,y-1))
    if x < size-1:
        adjPos.append((x+1,y))
    if y < size-1:
        adjPos.append((x,y+1))    
    return adjPos

def isPosInNodes(pos,nodes):
    for node in nodes:
        if pos == node.pos:
            return node
    return False

def existsInLowerCost(nodes,nodePos,cost):
    for node in nodes:
        if node.pos == nodePos and cost >= node.cost:
            return True
    return False

def nodeFitness(n):
    return n.cost + n.heur


size = data.shape[0]

data_expanded = np.zeros([size*5,size*5],dtype='uint64')

for i in range(5):
    for j in range(5):
        data_expanded[i*size:(i+1)*size,j*size:(j+1)*size] = data + i + j
data_expanded[data_expanded > 9] = data_expanded[data_expanded > 9] - 9

data = data_expanded
size = data.shape[0]
endPos = (size-1,size-1)
startPos = (0,0)
openNodes = PriorityQueue()
openNodes.put(Node(startPos,0,computeHeuristic(startPos,endPos)))
# static lists/arrays because dynamic is really slow !
closeNodes = [[False]*size]*size
costDict = np.ones([size,size],dtype='uint64')*np.iinfo(np.uint64()).max
while openNodes:
    currentNode = openNodes.get()

    if currentNode.pos == endPos:
        print(currentNode.cost) # 652
        break
    
    for nodePos in adjacentPositions(currentNode.pos,size):
        x,y = nodePos
        cost = currentNode.cost + data[x,y]
        if not nodePos in closeNodes and not costDict[nodePos[0],nodePos[1]] < cost:
            node = Node(nodePos,cost,computeHeuristic(nodePos, endPos),currentNode)
            openNodes.put(node)
            costDict[nodePos[0],nodePos[1]] = cost
            
    closeNodes[currentNode.pos[0]][currentNode.pos[1]] = True
    