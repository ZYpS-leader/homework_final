import statsmodels.api as sm
import pandas as pd
import numpy as np
def st():
    mode=input("请选择输入模式:1代表手动输入列表;2代表指定csv文件.")
    if mode == "1":
        la=input("特征组: > ")
        lb=input("目标组: > ")
    elif mode == "2":
        print("注意!csv中数据必须满足:第一列全部为特征组;第二列全部为目标组.不允许有行名.第一列列名必须为'特征组',第二列列名必须为'目标组'.")
        path=input("csv路径: > ")     
        la=pd.read_csv(path,usecols=['特征组'] )
        lb=pd.read_csv(path,usecols=["目标组"]) 
    la1=list(la["特征组"])
    lb1=list(lb["目标组"])
    X=la1
    Y=lb1
    dX=np.column_stack((X,np.power(X,2),np.power(X,3),np.power(X,4),np.sin(X),np.tan(X),np.cos(X)  ))
    X_added=sm.add_constant(dX)
    model=sm.OLS(Y,X_added)
    results=model.fit() 
    print("本次精度为",results.rsquared*100,"%") 
    x=int(input('需要预测的特征组为:'))
    p=results.predict([1,x,np.power(x,2),np.power(x,3),np.power(x,4),np.sin(x),np.tan(x),np.cos(x)])
    print(p)