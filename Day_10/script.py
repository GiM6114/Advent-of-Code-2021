from collections import deque

with open('input.txt','r') as f:
    data = f.readlines()

# =============================================================================
# PART 1 & PART 2 (lets do everything in one pass !)
# =============================================================================

closers = {'(':')', '[':']', '{':'}', '<':'>'}
openers = {closer : opener for opener,closer in closers.items()}
values = {')':3, ']':57, '}':1197, '>':25137}
incompletedValues = {')':1, ']':2, '}':3, '>':4}

score = 0
incompletedScores = []
for line in data:
    stack = deque()
    corrupted = False
    for char in line:
        if char in openers.values():
            stack.append(char)
        elif char in closers.values():
            associatedOpener = openers[char]
            previousOpener = stack.pop()
            if associatedOpener != previousOpener:
                score += values[char]
                corrupted = True
                break
    if not corrupted:
        incompletedScore = 0
        for char in reversed(stack):
            incompletedScore *= 5
            incompletedScore += incompletedValues[closers[char]]
        incompletedScores.append(incompletedScore)
    

print(score) # 316,851
incompletedScores.sort()
print(incompletedScores[len(incompletedScores)//2]) # 2,182,912,364 