import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("C:/Users/laddu/Downloads/graduate-admissions/Admission_Predict.csv")
#print(data)
X=data.iloc[:,:-1].values
y=data.iloc[:,-1].values
#print(X)
from sklearn.preprocessing import LabelEncoder
laben=LabelEncoder()
X[:,3]=laben.fit_transform(X[:,3])
#print(X)
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

print(X_train)
print(y_test)

