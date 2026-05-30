import numpy as np
from numpy.polynomial.chebyshev import chebfit
__all__=['mdeviation','mdevsq','moutlier','mregression']
def mdeviation(data):
 '''`data`の偏差値を求める'''
 std=10/np.std(data)
 mean=np.mean(data)
 return(std*(data-mean))+50
def mdevsq(data):
 '''偏差平方和を求める'''
 mean=np.mean(data)
 return np.sum((data-mean)**2)
def moutlier(data):
 '''外れ値を求める'''
 q1,q3=np.percentile(data,[25,75])
 iqr=(q3-q1)*1.5
 return data[(data<(q1-iqr))|(data>(q3+iqr))]
def mregression(x:np.ndarray,y:np.ndarray,n:int=1):
 '''(x,y)の回帰直線を求める。'''
 return chebfit(x,y,n)