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

#Transformation of non numneric cloumns to 1-Hot Encoded columns
#There is an exception with the Pclass. Though it's co-incidentally a number column but it's a Categoric column(Even common-sence wise).

#Transform categoric to One hot encoding using get_dummies
 titanic_train1= pd.get_dummies(titanic_train, columns=['Pclass','Sex','Embarked'])
titanic_train1.shape
titanic_train1.info()
titanic_train1.describe()


#now the drop non numerical columns where we will not be applying logic. Something like we will not apply logic on names, passengerID ticket id etc...

X_Train =titanic_train1.drop(['PassengerId','Age','Cabin','Ticket','Name','Survived'],1)

X_Train.info()
X_Train.shape
Y_Train=titanic_train['Survived']

#Build the decision tree model
dt = tree.DecisionTreeClassifier()
dt.fit(X_Train,Y_Train)



os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
os.getcwd()

#visualize the decission tree
    dot_data = io.StringIO()  
    tree.export_graphviz(dt, out_file = dot_data, feature_names = X_Train.columns)
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())#[0]
    graph.write_pdf("DecissionTree1.pdf")


# Read the Titanic Test Data

titanic_test=pd.read_csv('C:/Users/KARTDH/Desktop/DS/GV-S/titanic/test.csv')

titanic_test.shape
titanic_test.info()


titanic_test.shape
#Fill missing data of Test(Fare)
titanic_test.info() #Found that one row has Fare = null in test data. Instead of dropping this column, let's take the mean of it.
#Data Imputation

titanic_test.Fare[titanic_test['Fare'].isnull()]=titanic_test['Fare'].mean()

X_titanic_test=titanic_test[['Pclass', 'SibSp', 'Parch']]

#Predicting the output using the model which we built.

titanic_test['Survived']= dt.predict(X_titanic_test)
 os.getcwd()
 os.chdir('C:/Users/KARTDH/Desktop/DS/GV-S/')


titanic_test.to_csv("DecisionTreeOutput.csv",columns=['PassengerId', 'Survived'],index=False)


#Now apply same get_dummies and drop columns on test data as well like above we did for train data
titanic_test1 = pd.get_dummies(titanic_test, columns=['Pclass', 'Sex', 'Embarked'])
X_test = titanic_test1.drop(['PassengerId','Age','Cabin','Ticket', 'Name','Survived'], 1)


#Apply the model on future/test data

X_test.shape
X_test.info()
titanic_test['Survived'] = dt.predict(X_test)
os.getcwd()
titanic_test.to_csv("DecisionTree2.csv", columns=['PassengerId', 'Survived'], index=False)

