from datetime import date, datetime, time

import numpy as np
from dateutil.parser import parse

from ._time import times

__all__=['timeslist']
class timeslist:
 def __init__(self,dates):
  if isinstance(dates,np.ndarray):
   self.datelist=dates.astype('datetime64')
  elif isinstance(dates,list|tuple):
   dates=np.array(dates)
   if len(dates.shape)==1:
    self.datelist=np.array([d for d in self._serch_time(dates)])
   else:
    raise TypeError('一次元配列で指定してください')
  elif isinstance(dates,(str,datetime,date,times)):
   self.datelist=self._serch_time(dates)
  else:
   self.datelist=np.array([])
  self.datelist=self.datelist.astype('datetime64')
 def _serch_time(self,arr):
  arrs=np.array([])
  def _time_change(i):
   if isinstance(i,str):return np.array([parse(i)])
   elif isinstance(i,times):return np.array([i.datetimes])
   elif isinstance(i,datetime):return np.array([i])
   elif isinstance(i,date):return np.array([datetime.combine(i,time())])
  if isinstance(arr,np.ndarray):
   for i in arr:arrs=np.append(arrs,_time_change(i))
  else:arrs=_time_change(arr)
  return arrs
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