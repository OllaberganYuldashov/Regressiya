import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt


f=pd.read_csv('data.csv')
data=f.to_dict()

new_data=[]
#print(data['temp'][1])
l=len(data['temp'])
#print(l)

for i in range(l):
    if((int(data['temp'][i])>0) and (int(data['temp'][i])<100) and (int(data['nam'][i])>0) and (int(data['nam'][i])<100)):
        new_data.append([data['temp'][i],data['nam'][i],data['suv'][i]])
#print(new_data)



df=pd.DataFrame(new_data,columns=['temp','nam','suv'])
x=df[['temp','nam']]
y=df['suv']

print((df))

reg=linear_model.LinearRegression()
reg.fit(x,y)


print(reg.coef_)
print(reg.intercept_)


ax = plt.figure().add_subplot(projection='3d')
ax.plot(df[['temp']],df[['nam']],df[['suv']])
plt.show()