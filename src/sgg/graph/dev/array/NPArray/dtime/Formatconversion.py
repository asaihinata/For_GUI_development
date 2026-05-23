from dateutil.parser import parse
from numpy import array,ndarray,nditer,vectorize
from ..base import NPArray
from .data import serch_dtype
__all__=['Formatconversion']
class Formatconversion(NPArray):
 def __init__(self,data,dtype='datetime64[ms]',yearfirst=False,dayfirst=False):
  dtype=serch_dtype(dtype)
  if not isinstance(data,ndarray):data=array(data)
  self.yearfirst=yearfirst
  self.dayfirst=dayfirst
  func=vectorize(lambda strs,yearfirst,dayfirst:parse(str(strs),yearfirst=yearfirst,dayfirst=dayfirst))
  super().__init__(array([func(i,self.yearfirst,self.dayfirst)for i in nditer(data)],dtype=dtype).reshape(data.shape),dtype)