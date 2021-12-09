import numpy as np

with open('input.txt', 'r') as f:
    lanterns = np.loadtxt(f,delimiter=',',dtype='uint8')


# =============================================================================
# PART 1
# =============================================================================

# def simulateDay(lanterns):
#     lanternsToAdd = 0
#     for k in range(len(lanterns)):
#         if lanterns[k] == 0:
#             lanternsToAdd += 1
#             lanterns[k] = 6
#         else:
#             lanterns[k] -= 1
    
#     lanterns = np.append(lanterns,[8]*lanternsToAdd) # all at the end because append is slow
#     return lanterns

# nbDays = 80
# for i in range(nbDays):
#     lanterns = simulateDay(lanterns)

    
# nbLanterns = len(lanterns)
# print(nbLanterns) # 388,419

# =============================================================================
# PART 2
# =============================================================================

# better optimlization

def simulateDayOpti(lanternsSum):
    lanterns0 = lanternsSum[0]
    for idx in range(len(lanternsSum[:-1])):
        lanternsSum[idx] = lanternsSum[idx+1]
    lanternsSum[6] += lanterns0
    lanternsSum[8] = lanterns0
    return lanternsSum

lanternsSum = [0]*9
for lantern in lanterns:
    lanternsSum[lantern] += 1

nbDays = 256
for i in range(nbDays):
    lanternsSum = simulateDayOpti(lanternsSum)
    
nbLanterns = sum(lanternsSum)
print(nbLanterns) # 1,740,449,478,328