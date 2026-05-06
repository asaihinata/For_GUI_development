from .....developer import Number

__all__=['list2float','num0','num0s','num1s','listchose','range_zero_one']
def range_zero_one(val,out=1.0,endpoint=True):
 if not isinstance(val,int|float):return out
 if not isinstance(endpoint,bool):endpoint=True
 if endpoint and 0<=val<=1:return val
 elif not endpoint and 0<=val<1:return val
 return out
def num1s(val=0,mins=1):
 if isinstance(val,int|float|Number) and 1<=val:return val
 return mins
def num0s(val=0,mins=0):
 if isinstance(val,int|float|Number)and 0<=val:return val
 return mins
def num0(val=0,mins=0):
 if isinstance(val,int|float|Number)and 0<val:return val
 return mins
def list2float(lin=None):
 if isinstance(lin,list|tuple) and len(lin)==2 and all(isinstance(i,float)for i in lin):return True
 return False
def listchose(val,arr,other=None):
 if isinstance(arr,tuple|list)and other==None:other=arr[0]
 elif not isinstance(arr,tuple|list)and other==None:other=arr
 if val in arr:return val
 return other