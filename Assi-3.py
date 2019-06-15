'''
Question::
    Find addition,subtraction and multiplication and divison of two arrays
'''
#Solution::
import numpy as ny
x=ny.array([1,2,3,4])
y=ny.array([5.5,6.5,7.5,8.5])

print("sum=",ny.add(x,y))
print("mul=",ny.multiply(x,y))
print("sub=",ny.subtract(x,y))
print("div=",ny.divide(x,y))

'''
 Output::sum= [ 6.5  8.5 10.5 12.5]
         mul= [ 5.5 13.  22.5 34. ]
         sub= [-4.5 -4.5 -4.5 -4.5]
         div= [0.18181818 0.30769231 0.4        0.47058824]
'''
'''
Question::
    Find square root,max and min for column and row.
'''
#Solution
z=ny.array([[1,2],[3,4]])
print("Sqt=",ny.sqrt(z))
print("Max:",z.max(axis=0))
print("Max:",z.max(axis=1))
print("Min:",z.min(axis=0))
print("Min:",z.min(axis=1))

'''
 Output:
     Sqt= [[1.         1.41421356]
            [1.73205081 2.        ]]
     Max: [3 4]
     Max: [2 4]
     Min: [1 2]
     Min: [1 3]
'''     