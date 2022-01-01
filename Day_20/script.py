import numpy as np

data = open('input.txt','r').read()
data = data.replace('.','0').replace('#','1')
data = data.split('\n')
data.remove('')
data = [list(map(int,line)) for line in data[:-1]]

algo = data[0]
img = np.array(data[1:],dtype='int8')
n,m = img.shape

def PrintImage(img):
    n,m = img.shape
    for i in range(n):
        for j in range(m):
            print('#' if img[i,j] else '.',end='')
        print('\n',end='')

def ApplyAlgo(i,j,img,algo):
    binaryStr = str(img[i-1:i+2,j-1:j+2].flatten())[1:-1].replace(' ','')
    index = int(binaryStr,2)
    return algo[index]

def ImageEnhancement(img,algo):
    n,m = img.shape
    resultImg = img.copy()
    for i in range(1,n-1):
        for j in range(1,m-1):
            resultImg[i,j] = ApplyAlgo(i,j,img,algo)
    
    infinityValue = algo[0 if not resultImg[0,0] else len(algo)-1]
    resultImg[:,0]   = infinityValue
    resultImg[0,:]   = infinityValue
    resultImg[n-1,:] = infinityValue
    resultImg[:,m-1] = infinityValue
    return resultImg

b = 100 # border size
nB,mB = n+b*2,m+b*2
imgBigger = np.zeros([nB,mB],dtype='uint16')
imgBigger[b:n+b,b:m+b] = img

for i in range(50):
    imgBigger = ImageEnhancement(imgBigger, algo)
    # 5,301 for 2, 19,492 for 50

print(sum(sum(imgBigger)))
