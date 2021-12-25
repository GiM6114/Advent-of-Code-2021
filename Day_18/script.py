from math import floor,ceil

data = open('input.txt','r').readlines()

class Node:
    
    def __init__(self,l=None,r=None,p=None,v=None):
        self.l = l
        self.r = r
        self.p = p
        self.v = v
    
    @property
    def magnitude(self):
        if self.isLeaf():
            return self.v
        return 3*self.l.magnitude + 2*self.r.magnitude
        
    def __add__(self,other):
        result = Node(self,other)
        while True:
            if result.explode():
                continue
            if not result.split():
                break
        return result        
    
    @property
    def l(self):
        return self._l
    @l.setter
    def l(self,l):
        if isinstance(l,list):
            self._l = Node(l=l[0],r=l[1],p=self)
        elif isinstance(l,int):
            self._l = Node(p=self,v=l)
        elif isinstance(l,Node):
            self._l = l
            self._l.p = self
        else:
            self._l = l
            
    @property
    def r(self):
        return self._r
    @r.setter
    def r(self,r):
        if isinstance(r,list):
            self._r = Node(l=r[0],r=r[1],p=self)
        elif isinstance(r,int):
            self._r = Node(p=self,v=r)
        elif isinstance(r,Node):
            self._r = r
            self._r.p = self
        else:
            self._r = r
            
    def __str__(self):
        if self.isLeaf():
            return str(self.v)
        return f'[{self.l},{self.r}]'
    
    def isLeaf(self):
        return self.v is not None
    
    def isBeforeLeaves(self):
        return not self.isLeaf() and self.l.isLeaf() and self.r.isLeaf()
    
    def isRoot(self):
        return self.p is None
    
    def explode(self,depth=0):
        if depth < 4:
            if self.isLeaf():
                return False    
            exploded = self.l.explode(depth+1)
            if not exploded:
                exploded = self.r.explode(depth+1)
            return exploded
        elif depth == 4:
            if not self.isRoot() and self.isBeforeLeaves():
                self.p.addClosestLeft(self,self.l.v)
                self.p.addClosestRight(self,self.r.v)
                newNode = Node(p=self.p,v=0)
                self.__dict__.update(newNode.__dict__)
                return True
        return False
    
    def addClosestRight(self,caller,value):
        if not self.isRoot() and caller is self.r:
            self.p.addClosestRight(self,value)
        elif caller is self.l:
            self.r.addClosestRight(self,value)
        elif caller is self.p:
            if self.isLeaf():
                self.v += value
            else:
                self.l.addClosestRight(self,value)
    
    def addClosestLeft(self,caller,value):
        if not self.isRoot() and caller is self.l:
            self.p.addClosestLeft(self,value)
        elif caller is self.r:
            self.l.addClosestLeft(self,value)
        elif caller is self.p:
            if self.isLeaf():
                self.v += value
            else:
                self.r.addClosestLeft(self,value)
            
    def split(self):
        if self.isLeaf():
            if self.v >= 10:
                self.l = Node(p=self,v=floor(self.v/2))
                self.r = Node(p=self,v=ceil(self.v/2))
                self.v = None
                return True
        else:
            split = self.l.split()
            if not split:
                split = self.r.split()
            return split
            
# =============================================================================
# PART 1
# =============================================================================

snailfishNumbers = [eval(line) for line in data]
s = snailfishNumbers[0]
root = Node(l=s[0],r=s[1])
for snailfishNumber in snailfishNumbers[1:]:
    root += snailfishNumber
    
print(root.magnitude) # 3,699
    
# =============================================================================
# PART 2
# =============================================================================

maxMagnitude = 0
for n1 in snailfishNumbers:
    for n2 in snailfishNumbers:
        magnitude = (Node(n1[0],n1[1])+Node(n2[0],n2[1])).magnitude
        if magnitude > maxMagnitude:
            maxMagnitude = magnitude
            
print(maxMagnitude) # 4,735