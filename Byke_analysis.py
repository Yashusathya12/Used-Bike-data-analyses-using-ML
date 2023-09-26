import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
#data acquire
dataset=pd.read_csv("Used_Bikes.csv")
#dataset information
#dataset.info()
#print(dataset.iloc[0:10])

#data cleaning
#sns.heatmap(dataset.isnull())
#plt.show()
dataset.drop(['bike_name','city'],axis=1,inplace=True)
#print(dataset)
#City=pd.get_dummies(dataset['city'],drop_first=True)
#print(City)
Owner=pd.get_dummies(dataset['owner'],drop_first=True)
#print(Owner)
Brand=pd.get_dummies(dataset['brand'],drop_first=True)
#print(Brand)
dataset.drop(['owner','brand'],axis=1,inplace=True)
#print(dataset)
dataset=pd.concat([dataset,Owner,Brand],axis=1)
#print(dataset.iloc[5])
#print(dataset)
#splitting data as training and testing
x=dataset.iloc[:,1:].values
#print(x)
y=dataset.price
#print(x)
#training data
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=0.20,random_state=11)
#print(X_train)

from sklearn.linear_model import LinearRegression
reg=LinearRegression()
reg.fit(X_train,Y_train)
y_pred = reg.predict(X_test)
#print(y_pred)

print(pd.DataFrame(y_pred,Y_test))

from sklearn.metrics import mean_squared_error
#print(mean_squared_error(Y_test,y_pred))
#print(reg.score(X_test,Y_test))
#print(reg.intercept_)
#print(reg.coef_)


#prediction graph
plt.scatter(Y_test,y_pred,color='g')
plt.xlabel("Y_test")
plt.ylabel("Prediction")
plt.show()
