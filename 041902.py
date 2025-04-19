import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('./Salary_Data.csv')
x=data['YearsExperience']
y=data['Salary']

def plot_pred(w,b):
  y_pred = x * w + b
  plt.scatter(x,y, color='red',label='真實數據')
  plt.xlabel('年資',fontproperties='Microsoft YaHei')
  plt.ylabel('薪水',fontproperties='Microsoft YaHei')
  plt.title('年資-薪水',fontproperties='Microsoft YaHei')
  plt.plot(x, y_pred, color='blue', label='預測線')
  plt.legend(prop={'family': "Microsoft YaHei"})
  plt.xlim([0,12])
  plt.ylim([0,140])
  plt.show()

plot_pred(10,20)