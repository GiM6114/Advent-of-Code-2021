with open('input.txt', 'r') as f:
    reports = f.read()

reports = reports.split('\n')[:-1]


# =============================================================================
# PART 1
# =============================================================================

nbLines = len(reports)
halfNbLines = nbLines // 2
nbBits  = len(reports[0])

gammaBinary = '0b'
for i in range(nbBits):
    nbOnes = sum(list(map(
        lambda x : int(x[i]),reports
        )))
    gammaBinary += '1' if nbOnes > halfNbLines else '0'

gamma = int(gammaBinary,2)
epsilon = int('0b'+'1'*nbBits,2) - gamma

powerConsumption = gamma*epsilon
print(powerConsumption) # 3,958,454

# =============================================================================
# PART 2
# =============================================================================

def getRemainers(previousRemainers,leastCommon,defaultValue):
    
    nbOnes = sum(list(map(
        lambda x : int(x[i]),previousRemainers
        )))
    
    halfLen = len(previousRemainers)/2
    
    if nbOnes > halfLen:
        mostCommonValue = '0' if leastCommon else '1'
    elif nbOnes < halfLen:
        mostCommonValue = '1' if leastCommon else '0'
    else:
        mostCommonValue = defaultValue
        
    
    remainers = list(filter(lambda x : x[i] == mostCommonValue,previousRemainers))
    return remainers

    
remainersOxygen = reports[:]
remainersCO2 = reports[:]
valueOxygen = -1
valueCO2 = -1

for i in range(nbBits):
    
    if valueOxygen == -1:
        remainersOxygen = getRemainers(remainersOxygen,False,'1')
        print(remainersOxygen)
    if valueCO2 == -1:
        remainersCO2 = getRemainers(remainersCO2,True,'0')
            
    if len(remainersOxygen) == 1:
        valueOxygen = remainersOxygen[0]
        
    if len(remainersCO2) == 1:
        valueCO2 = remainersCO2[0]
    
    if valueOxygen != -1 and valueCO2 != -1:
        break

print(valueOxygen, valueCO2)
print(int(valueOxygen,2) * int(valueCO2,2)) # 1,613,181