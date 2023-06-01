import statsmodels.api as sm
import pandas as pd
import numpy as np
def st(path,x:float):      
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
    p1="本次精度为"+str(results.rsquared*100)+"%"   
    p2=results.predict([1,x,np.power(x,2),np.power(x,3),np.power(x,4),np.sin(x),np.tan(x),np.cos(x)])
    return p1,p2
