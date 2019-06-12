
#Find addition,subtraction,multiplication and division of two arrays

import numpy as np
K=np.array([1,2,3,4])
L=np.array([5.5,6.5,7.5,8.5])
print(np.add(K,L))

    
print(np.subtract(K,L))

print(np.multiply(K,L))

print(np.divide(K,L))


'''
output: [ 6.5  8.5 10.5 12.5]
[-4.5 -4.5 -4.5 -4.5]
[ 5.5 13.  22.5 34. ]
[0.18181818 0.30769231 0.4        0.47058824] '''

#Find square root,max and min for column and row,median,mean,std and exp

X = np.array([[1,2],[3,4]])
print(np.sqrt(X))

print(np.min(X,axis=1))

print(np.max(X,axis=1))

print(np.min(X,axis=0))

print(np.max(X,axis=0))

print(X.std())

print(np.exp(X))

print(X.mean())

print(np.median(X))

'''
output: [[1.         1.41421356]
 [1.73205081 2.        ]]
[1 3]
[2 4]
[1 2]
[3 4]
1.118033988749895
[[ 2.71828183  7.3890561 ]
 [20.08553692 54.59815003]]
2.5
2.5 '''





