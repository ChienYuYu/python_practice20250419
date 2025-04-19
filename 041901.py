import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('./Salary_Data.csv')
x=data['YearsExperience']
y=data['Salary']

plt.scatter(x,y)
plt.xlabel('Year')
plt.ylabel('Salary')
plt.show()