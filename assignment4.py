

import numpy as np
import pandas as pd
a=[{'year':1990,'name':'Alice','department':'HR','age':25,'salary':50000},{'year':1990,'name':'Bob','department':'RD','age':30,'salary':48000},{'year':1990,'name':'Charlie','department':'Admin','age':45,'salary':55000},{'year':1991,'name':'Alice','department':'HR','age':26,'salary':52000},{'year':1991,'name':'Bob','department':'RD','age':31,'salary':50000},{'year':1991,'name':'Charlie','department':'Admin','age':46,'salary':60000},{'year':1992,'name':'Alice','department':'HR','age':27,'salary':60000},{'year':1992,'name':'Bob','department':'RD','age':32,'salary':52000},{'year':1992,'name':'Charlie','department':'Admin','age':47,'salary':62000}]
data=pd.DataFrame(a,index=['0','1','2','3','4','5','6','7','8'])
data

data.groupby(['year'])['salary'].sum()

data.groupby(['name'])['salary'].sum()

data.groupby(['department','year'])['salary'].sum()


import pandas as pd
empl=[{'year':1990,'name':"alice",'dept':"HR",'age':25,'salary':25000},
     {'year':1990,'name':"bob",'dept':"RD",'age':30,'salary':480000},
     {'year':1990,'name':"charlie",'dept':"admin",'age':40,'salary':55000},
     {'year':1991,'name':"alice",'dept':"HR",'age':26,'salary':52000},
     {'year':1991,'name':"bob",'dept':"RD",'age':26,'salary':50000},
     {'year':1991,'name':"charlie",'dept':"admin",'age':46,'salary':60000},
     {'year':1992,'name':"alice",'dept':"HR",'age':27,'salary':60000},
     {'year':1992,'name':"bob",'dept':"RD",'age':32,'salary':60000},
     {'year':1992,'name':"charlie",'dept':"admin",'age':28,'salary':60000}]

data=pd.DataFrame(empl)
data
data.groupby(['year'])['salary'].sum()
data.groupby(['name'])['salary'].sum()
data.groupby(['dept','year'])['salary'].sum()

