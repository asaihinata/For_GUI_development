from dateutil.parser import parse
from numpy import array,ndarray,nditer,vectorize
from ...base import NPArray
from ..data import serch_dtype
__all__=['Formatconversion','strconversions','conversions']
def strconversions(formatstr,year=False,day=False):
 return str(parse(formatstr,yearfirst=year,dayfirst=day))
def conversions(formatstr,year=False,day=False):
 return parse(formatstr,yearfirst=year,dayfirst=day)
class Formatconversion(NPArray):
 def __init__(self,data,dtype='datetime64[D]',yearfirst=False,dayfirst=False):
  dtype=serch_dtype(dtype)
  if not isinstance(data,ndarray):data=array(data)
  self.yearfirst=yearfirst
  self.dayfirst=dayfirst
  func=vectorize(lambda strs,yearfirst,dayfirst:strconversions(str(strs),year=yearfirst,day=dayfirst))
  super().__init__(array([func(i,self.yearfirst,self.dayfirst)for i in nditer(data)],dtype=dtype).reshape(data.shape),dtype)