__all__=['allNone','allNones','list2num','list2int','list2float','list4num','list4int','list4float','typelist','listchose']
def allNone(a,b=None):return True if a is None and b is None else False
def allNones(a,b=None,other=None):
 if (a is not None and b is not None) or (a is not None and b is None):return a
 elif (a is None and b is not None):return b
 return other
def list2num(lin=None):return True if isinstance(lin,list|tuple) and len(lin)==2 and all(isinstance(i,int|float)for i in lin) else False
def list2int(lin=None):return True if isinstance(lin,list|tuple) and len(lin)==2 and all(isinstance(i,int)for i in lin) else False
def list2float(lin=None):return True if isinstance(lin,list|tuple) and len(lin)==2 and all(isinstance(i,float)for i in lin) else False
def list4num(lin=None):return True if isinstance(lin,list|tuple) and len(lin)==4 and all(isinstance(i,int|float)for i in lin) else False
def list4int(lin=None):return True if isinstance(lin,list|tuple) and len(lin)==4 and all(isinstance(i,int)for i in lin) else False
def list4float(lin=None):return True if isinstance(lin,list|tuple) and len(lin)==4 and all(isinstance(i,float)for i in lin) else False
def typelist(val):
 if isinstance(val,tuple|list):return True
 return False
def listchose(val,arr,other=None):
 if isinstance(arr,tuple|list)and other==None:other=arr[0]
 elif not isinstance(arr,tuple|list)and other==None:other=arr
 if val in arr:return val
 return other