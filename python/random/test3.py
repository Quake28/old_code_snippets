array=[10,20,30,40,50,60]
def rotateLeft(source, k):
    temp= []
    for j in range(0,k):
        temp.append(source[j])
    for i in range(k, len(array)):
        source[i-k]=source[i]
    for l in range(k):
        source[k+l]=temp[l]
    return source
print(rotateLeft(array,3))


import numpy as np
array= np.array([10,20,30,40,50,60])
def rotateLeft(source, k):
    temp= []
    for j in range(0,k):
        temp.append(source[j])
    for i in range(k, len(array)):
        source[i-k]=source[i]
        source[i]= temp[j]
        j-=1
    return source
print(rotateLeft(array,3))
