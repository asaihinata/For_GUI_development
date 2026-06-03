import numpy as np
from numpy.polynomial.chebyshev import chebfit,chebval
__all__=['mdeviation','mdevsq','moutlier','mregression','mone_regression','mFregression']
def mdeviation(data):
 std,mean=10/np.std(data),np.mean(data)
 return(std*(data-mean))+50
def mdevsq(data):
 mean=np.mean(data)
 return np.sum((data-mean)**2)
def moutlier(data):
 q1,q3=np.percentile(data,[25,75])
 iqr=(q3-q1)*1.5
 return data[(data<(q1-iqr))|(data>(q3+iqr))]
def mFregression(x,y,Fx,n=1):return chebval(Fx,chebfit(x,y,n))
def mregression(x,y,n=1):
 return chebfit(x,y,n)
def mone_regression(x,y):
 return chebfit(x,y,1)