#
# Got this beatufiful solution from
# @ProfessorXmonad on Twitter
#

import numpy as np
from numpy.linalg import matrix_power

lines = open('input.txt').read().split('\n')[:-1]
poly, rules = lines[0],lines[2:]
    
subst = {}

# Build the list of all atoms in the data
atoms = list(set(poly))
for r in rules:
    pair,atom = r.split(' -> ')
    if atom not in atoms:
        atoms.append(atom)
        
atoms.sort()
natoms = len(atoms)

# Map a number to each atom
i_atoms = { a:i for i,a in enumerate(atoms)}
# Map a number to each pair of atoms
def idx(a,b):
    return i_atoms[a]*natoms + i_atoms[b]

# For every pair 'XY', m[idx('X','Y')] will hold the
# number of pair 'XY' in the string.
m = np.zeros(natoms*natoms,dtype='uint64')
for i in range(len(poly)-1):
    m[idx(*poly[i:i+2])] += 1
  
# m_repl will be filled with 0 except at places where there is
# a rule that a pair (row) will build another pair
# Ex : If there is a rule BC -> N then :
    #   m_repl[idx(BC),idx(BN)] = 1
    # because every time the rule is applied, a BN is constructed
    # (same for NC !)
m_repl = np.zeros((natoms*natoms,natoms*natoms),dtype='uint64')
for r in rules:
    (a,b), c = r.split(' -> ')
    m_repl[idx(a,b),idx(a,c)] += 1
    m_repl[idx(a,b),idx(c,b)] += 1
    
m_repl = m_repl.transpose()

# Linear algebra computation to speed up the process
res = matrix_power(m_repl,40) @ m.transpose()

count = []
for a in atoms:
    c = np.uint64(0)
    for b in atoms:
        c += res[idx(a,b)] + res[idx(b,a)]
    if a in [poly[0],poly[-1]]:
        c += 1
    count.append(c // 2)
    
print('Max - min : ',max(count)-min(count))