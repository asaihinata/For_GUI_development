from ._darray import *
from ._dcolor import *
from ._dnumber import *
def args(*args,data=None,x=None,y=None):
 lens=len(args)
 if lens==1:data=args[0]
 elif lens==2:x,y=args[0],args[1]
 elif lens>2:
  raise ValueError('argsは最大2つまで指定してください')
 if (data is not None and (x is not None or y is not None)) or (data is None and (x is None or y is None)):
  raise ValueError('組み合わせが不正です')
 return(data,x,y)
def bols(j,o=True):
 if isinstance(j,bool):return j
 return o