# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 21:13:06 2019

@author: DELL
"""
#assignment 1
dict={'keys':['shanghai','intanbul','hyderabad'],'value':[17,18,19]}
dict


#assignment 2
answer = 20
guess = int(input('enter the number you have guessed\n'))
difference = answer-guess
if difference < -30:
    print("too hight")
if difference<0 and difference >- 30:
    print("just high")
if difference < 20 and difference >0 :
    print("just low")
if difference>0 and difference > 30:
    print("too low")
    
#assignment 2 2nd problem
for i in range(0,30+1):
    if(i%5==0):
        print(i)
 
#assignment2 3rd problem
interlimit = int(input("enter the number for which you want to find the nearest square"))
i=1
while(i*i<interlimit):
    i=i+1
i=i-1
print(i)    
    
#assignment 3 part 1
x=np.array([1,2,3,4])
y=np.array([5.5,6.5,7.5,8.5])
print(np.add(x,y))
print(np.subtract(x,y))
print(np.multiply(x,y))
print(np.divide(x,y))


#assignment 3 part 2
x=np.array([[1,2],[3,4]])
print(np.sqrt(x[:,:1]),"\n")
print(np.sqrt(x[1:,:]))
print(np.max(x, axis=0))
print(x.max(axis=0))
print(np.max(x, axis=1))
print(np.min(x, axis=0))
print(np.min(x, axis=1))
print(np.median(x))
print(np.std(x))
print(np.mean(x))
print(np.exp(x))
     
 
#assignment 4
data=[
    {
        'year': 1990, 'name' : 'Alice', 'department' : 'HR','Age':25, 'Salary':50000
    },
    {
        'year': 1990, 'name' : 'Bob', 'department' : 'RD','Age':30, 'Salary':48000
    },
    {
        'year': 1990, 'name' : 'Charlie', 'department' : 'Admin','Age':45, 'Salary':55000
    },
    {
        'year': 1991, 'name' : 'Alice', 'department' : 'HR','Age':26, 'Salary':52000
    },
    {
        'year': 1991, 'name' : 'Bob', 'department' : 'RD','Age':31, 'Salary':50000
    },
    {
        'year':1991, 'name' : 'Charlie', 'department' : 'Admin','Age':46, 'Salary':60000
    }, 
    {
        'year': 1992, 'name' : 'Alice', 'department' : 'HR','Age':27, 'Salary':60000
    },
    {
        'year':1992, 'name' : 'Bob', 'department' : 'RD','Age':32, 'Salary':52000
    },
    {
        'year':1992, 'name' : 'Charlie', 'department' : 'Admin','Age':28, 'Salary':62000
    }    
]
data_series=pd.DataFrame(data,index=[0,1,2,3,4,5,6,7,8])
data_series
print(data_series.groupby(['year'])['Salary'].sum())
print(data_series.groupby(['name'])['Salary'].sum())
print(data_series.groupby(['department','year'])['Salary'].sum())       