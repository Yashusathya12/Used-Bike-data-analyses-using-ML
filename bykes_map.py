

#histogram
#print(dataset)
#x= dataset.age
#y=dataset.kms_driven
#z=dataset.power
#l=dataset.price


#plt.subplot(221)
#plt.hist(x,color='r')
#plt.title('AGE OF BIKES')

#plt.subplot(222)
#plt.hist(y)
#plt.title('KMS DRIVEN')

#plt.subplot(223)
#plt.hist(z,color='y')
#plt.title('POWER')

#plt.subplot(224)
#plt.hist(l,color='g')
#plt.title('PRICE')
#plt.show()





#style.use("dark_background")

#bar chart
#x=dataset.age
#y=dataset.kms_driven
#plt.xlabel('age of bikes')
#plt.ylabel('kms driven')
#plt.bar(x,y,label='age v/s kms_driven',width=0.5)
#plt.legend()
#plt.grid(True,color='y')
#plt.show()



#scatter chart
#x=dataset.power
#y=dataset.price
#plt.xlabel('power')
#plt.ylabel('price')
#plt.scatter(x,y,c='g',label='power vs Price',s=20,marker='+')
#plt.legend()
#plt.show()


#horisontal bar chart
#x=dataset.age
#y=dataset.price
#plt.xlabel('price')
#plt.ylabel('age')
#plt.barh(x,y,label='age v/s price',height=0.5,color='y')
#plt.legend()
#plt.show()


#box plot
#plt.figure(figsize = (10,5))
#sns.boxplot(x="brand",y="price",data=dataset)
#plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import style

dataset=pd.read_csv("Used_Bikes.csv")
style.use("dark_background")

#pair plot
g=sns.pairplot(dataset)
g.map_upper(sns.scatterplot,color='red')
g.map_lower(sns.scatterplot, color='green')
g.map_diag(plt.hist)
plt.show()
