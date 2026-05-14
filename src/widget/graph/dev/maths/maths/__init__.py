import numpy as np
__all__=['sturges']
def sturges(n,type='ceil'):
 if isinstance(n,int):n=n
 elif isinstance(n,list|tuple):n=len(n)
 elif isinstance(n,np.ndarray):n=n.size
 else:
  raise TypeError('nには整数型か配列の型で指定してください')
 formula:float=1.0+np.log2(n)
 if type=='ceil':return np.ceil(formula)
 elif type=='floor':return np.floor(formula)
 else:return np.round(formula,0)