import pandas as pd
from sklearn import linear_model


f=pd.read_csv('data.csv')


x=f[['temp','nam']]
y=f['suv']


reg=linear_model.LinearRegression()
reg.fit(x,y)


print(reg.coef_)
print(reg.intercept_)

