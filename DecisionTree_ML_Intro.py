# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 22:33:59 2020

@author: kartdh
"""


import pandas as pd
from sklearn import tree 

import io #input output operations
import pydotplus #if we need to use any external .exe files....
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

titanic_train = pd.read_csv('C:/Users/KARTDH/Desktop/DS/GV-S/titanic/train.csv')

#EDA
titanic_train.shape
titanic_train.info()
titanic_train.describe()

#Let's start the journey with non categorical and non missing data columns
X_titanic_train=titanic_train[['Pclass', 'SibSp', 'Parch']] # X-Axis
Y_titanic_train=titanic_train['Survived'] # Y-Axis

#Build the decision tree model
dt = tree.DecisionTreeClassifier()
dt.fit(X_titanic_train,Y_titanic_train)

# Read the Titanic Test Data

titanic_test=pd.read_csv('C:/Users/KARTDH/Desktop/DS/GV-S/titanic/test.csv')

titanic_test.shape
titanic_test.info()

X_titanic_test=titanic_test[['Pclass', 'SibSp', 'Parch']]

#Predicting the output using the model which we built.

titanic_test['Survived']= dt.predict(X_titanic_test)
 os.getcwd()
 os.chdir('C:/Users/KARTDH/Desktop/DS/GV-S/')


titanic_test.to_csv("DecisionTreeOutput.csv",columns=['PassengerId', 'Survived'],index=False)


