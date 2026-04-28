from datetime import date,datetime,time
from ._time import times
__all__=['timeslist']
class timeslist:
 def __init__(self,dates,format='%Y/%m/%d,%H:%M:%S'):
  if isinstance(dates,(str,datetime,times,date)):self.datelist=[self._change(dates,format)]
  elif isinstance(dates,(list,tuple)):self.datelist=[self._change(d,format)for d in dates]
  else:self.datelist=[]
  self.datelist=tuple(self.datelist)
 def _change(self,dates,format):
  if isinstance(dates,datetime):return dates
  elif isinstance(dates,date):return datetime.combine(dates,time())
  elif isinstance(dates,times):return dates.strptime(format=format)
  elif isinstance(dates,str):return datetime.strptime(dates,format)
  return None
 @classmethod
 def __instancecheck__(cls,ins):return isinstance(ins,timeslist)
 def __len__(self):return len(self.datelist)
 def __iter__(self):return iter(self.datelist)
 def __getitem__(self,val):
  if isinstance(val,int):
   if 0<=val<len(self):return self.datelist[val]
   raise IndexError('配列の範囲外です')
  elif isinstance(val,slice):return self.datelist[val]
  raise TypeError('リストのインデックスはintまたはslicesである必要があります')