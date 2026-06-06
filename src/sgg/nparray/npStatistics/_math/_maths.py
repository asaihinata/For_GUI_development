import numpy as np
from numpy.linalg import norm
from numpy.polynomial.chebyshev import chebfit,chebval
__all__=['mdeviation','mdevsq','moutlier','mFregression','mregression','mone_regression','fisher_ztransformation','fzt_test_statistic','Euclidean_distance']
def __sr3(n):
 if not isinstance(n,int|float):
  raise TypeError('nには整数型を指定してください')
 elif n==3:
  raise ZeroDivisionError('nに3を指定できません')
 return np.sqrt(1/(n-3))
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
def mregression(x,y,n=1):return chebfit(x,y,n)
def mone_regression(x,y):return chebfit(x,y,1)
def fisher_ztransformation(r):return np.log((1+r)/(1-r))/2
def fzt_test_statistic(r,r0,n):
 rs=np.log((1+r)/(1-r))
 r0s=np.log((1+r0)/(1-r0))
 return 0.5*(rs-r0s)/__sr3(n)
def Euclidean_distance(a,b):return norm(np.array(b)-np.array(a))