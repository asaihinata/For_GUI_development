from math import ceil,floor
from os import system as sys
from platform import system
from sys import getsizeof
from numpy import array,ndarray
from numpy.random import choice,default_rng
__all__=['clear','LIST','Number','rand','rands','sort']
class clear:
 '''コンソールを削除する。'''
 def __init__(self):sys('cls' if system()=='Windows'else'clear')
 def __str__(self):return 'clear'
 @classmethod
 def __instancecheck__(cls,ins):return isinstance(ins,clear)
class rand:
 '''ランダムな値を生成する。'''
 def __init__(self):
  self.seeds=42
  self.rng=default_rng(seed=42)
 def __sizeof__(self):return super().__sizeof__()+getsizeof(self.rng)+getsizeof(self.seeds)
 @classmethod
 def __instancecheck__(cls,ins):return isinstance(ins,rand)
 @classmethod
 def seed(cls,seeds):
  if isinstance(seeds,int):cls.seeds,cls.rng=seeds,default_rng(seed=seeds)
 @classmethod
 def rand(cls,size=None):return cls._rand(size)
 @staticmethod
 def _rand(size):return rand.rng.random(size)
 @classmethod
 def randn(cls,size=None):return cls._randn(size)
 @staticmethod
 def _randn(size):return rand.rng.standard_normal(size)
 @classmethod
 def randint(cls,low=1,high=None,size=None,endpoint=False):return cls._randint(low,high=high,size=size,endpoint=endpoint)
 @staticmethod
 def _randint(low,high=None,size=None,endpoint=False):return rand.rng.integers(low,high=high,size=size,endpoint=endpoint)
 @classmethod
 def randrange(cls,min=0,max=1,size=None):
  if max<min:min,max=max,min
  return cls._randrange(min,max,size)
 @staticmethod
 def _randrange(low,high,size):return rand.rng.random(size)*(high-low)+low
 @classmethod
 def normal(cls,low=0,high=1,lenght=None,hierarchy=None):
  if isinstance(low,Number):low=low.val
  if isinstance(high,Number):high=high.val
  return cls.rng.normal(low,high,(hierarchy,lenght)) if isinstance(hierarchy,int) and 2<=hierarchy else cls.rng.normal(low,high,lenght)
 @classmethod
 def rands(cls,low=1,high=None,lenght=1,hierarchy=None):
  if isinstance(low,Number):low=low.val
  if isinstance(high,Number):high=high.val
  if high<low:high,high=high,low
  if isinstance(hierarchy,int) and 2<=hierarchy:return cls.rng.uniform(low=low,high=high,size=(hierarchy,lenght))
  else:return cls.rng.uniform(low=low,high=high,size=lenght)
 @classmethod
 def randsint(cls,low=1,high=None,lenght=1,hierarchy=None):
  if isinstance(low,Number):low=low.val
  if isinstance(high,Number):high=high.val
  if high<low:high,high=high,low
  if isinstance(hierarchy,int) and 2<=hierarchy:return cls.rng.integers(low=low,high=high,size=(hierarchy,lenght))
  else:return cls.rng.integers(low=low,high=high,size=lenght)
 @classmethod
 def listrand(cls,arr,size=None):
  return choice(array(list(arr)if isinstance(arr,LIST) else arr,dtype=object),size=size)
class rands:
 '''ランダムな値を生成する。'''
 def __init__(self,seed=42):
  if not isinstance(seed,int):seed=42
  self.seeds=seed
  self.rng=default_rng(seed=seed)
 def __sizeof__(self):return super().__sizeof__()+getsizeof(self.rng)+getsizeof(self.seeds)
 @classmethod
 def __instancecheck__(cls,ins):return isinstance(ins,rands)
 def seed(self,seed):
  if isinstance(seed,int):
   self.seeds=seed
   self.rng=default_rng(seed=seed)
 def rand(self,size=None):return self.rng.random(size)
 def randn(self,size=None):return self.rng.standard_normal(size)
 def randint(self,low=1,high=None,size=None,endpoint=False):
  return self.rng.integers(low,high=high,size=size,endpoint=endpoint)
 def randrange(self,min=0,max=1,size=None):
  if max<min:min,max=max,min
  return self.rng.random(size)*(max-min)+max
 def normal(self,low=0,high=1,lenght=None,hierarchy=None):
  if isinstance(low,Number):low=low.val
  if isinstance(high,Number):high=high.val
  if isinstance(hierarchy,int) and 2<=hierarchy:
   return self.rng.normal(low,high,(hierarchy,lenght))
  else:
   return self.rng.normal(low,high,lenght)
 def rands(self,low=1,high=None,lenght=1,hierarchy=None):
  if isinstance(low,Number):low=low.val
  if isinstance(high,Number):high=high.val
  if high<low:high,high=high,low
  if isinstance(hierarchy,int) and 2<=hierarchy:return self.rng.uniform(low=low,high=high,size=(hierarchy,lenght))
  else:return self.rng.uniform(low=low,high=high,size=lenght)
 def randsint(self,low=1,high=None,lenght=1,hierarchy=None):
  if isinstance(low,Number):low=low.val
  if isinstance(high,Number):high=high.val
  if high<low:high,high=high,low
  if isinstance(hierarchy,int) and 2<=hierarchy:return self.rng.integers(low=low,high=high,size=(hierarchy,lenght))
  else:return self.rng.integers(low=low,high=high,size=lenght)
 def listrand(self,arr,size=None):
  return choice(array(list(arr)if isinstance(arr,LIST) else arr,dtype=object),size=size)
class LIST:
 def __init__(self,lists,*arg):
  if isinstance(lists,list):self.lists=lists
  elif isinstance(lists,(tuple,range)):self.lists=list(lists)
  elif isinstance(lists,LIST):self.lists=lists.lists
  elif isinstance(lists,ndarray):self.lists=lists.tolist()
  else:self.lists=[lists]
  for i in arg:self.lists.append(i)
 @classmethod
 def __instancecheck__(cls,ins):return isinstance(ins,LIST)
 def __contains__(self,val):return val in self.lists
 def __len__(self):return len(self.lists)
 def __iter__(self):return iter(self.lists)
 def __reversed__(self):
  self.lists=reversed(self.lists)
  return self
 def __getitem__(self,val):
  if isinstance(val,int)and 0<=val<len(self):return self.lists[val]
  return self.lists[0]
 def __eq__(self,lists):
  lens,judge=len(self),True
  if isinstance(lists,LIST)and(len(lists)==lens):
   lists=list(lists)
   for i in range(lens):
    if self.lists[i]==lists[i]:
     judge=False
     break
  else:judge=False
  return judge
 def __ne__(self,lists):
  lens,judge=len(self),False
  if isinstance(lists,LIST)and(len(lists)==lens):
   lists=list(lists)
   for i in range(lens):
    if self.lists[i]!=lists[i]:
     judge=True
     break
  else:judge=True
  return judge
 def __add__(self,val):
  if isinstance(val,LIST):self.lists=self.lists+val.lists
  elif isinstance(val,(list,tuple)):
   for i in val:self.lists.append(i)
  else:self.lists.append(val)
  return self
 def __radd__(self,val):
  if isinstance(val,LIST):val=val.lists+self.lists
  else:
   if isinstance(val,tuple):val=list(val)
   elif not isinstance(val,list):val=[val]
   for i in self.lists:val.append(i)
  self.lists=val
  return self
 def __iadd__(self,val):
  if isinstance(val,LIST):self.lists=self.lists+val.lists
  elif isinstance(val,(range,list,tuple)):
   for i in list(val):self.lists.append(i)
  else:self.lists.append(val)
  return self
 def __mul__(self,val):
  if isinstance(val,int)and 1<=val:
   lin=self.lists
   for _ in range(val-1):self.lists=self.lists+lin
  return self
 def __getattribute__(self,name):return super().__getattribute__(name)
 def _flatten(self,lists):
  for i in lists:
   if isinstance(i,list):yield from self._flatten(i)
   else:yield i
 def append(self,*arg):
  for i in arg:self.lists.append(i)
 def clear(self):self.lists=[]
 def flatten(self):return list(self._flatten(self.lists))
 def get(self,val):
  if not isinstance(val,int):return self.lists[0]
  elif val<=0:val=abs(val)
  return(self.lists*(val//len(self.lists)+1))[:val]
 def sort(self,type=True):
  if not isinstance(type,bool):type=True
  self.lists=sort(self.lists,type)
  return self
class sort:
 def __init__(self,data,types=True):
  if not isinstance(data,(list,tuple,LIST)):
   raise TypeError('dataに配列の型を指定してください')
  if isinstance(data,LIST):data=data.lists
  self.order=types if isinstance(types,bool) else True
  self.data=sorted(data,key=sort._ascending) if self.order else sorted(data,key=sort._descending)
 @classmethod
 def __instancecheck__(cls,ins):return isinstance(ins,sort)
 def __contains__(self,val):return val in self.data
 def __iter__(self):return iter(self.data)
 def __bool__(self):return bool(self.order)
 def __len__(self):return len(self.data)
 def __reversed__(self):
  self.order=not self.order
  self.data=sorted(self.data,key=sort._ascending) if self.order else sorted(self.data,key=sort._descending)
  return self
 def __eq__(self,lists):
  lens,judge=len(self),True
  if isinstance(lists,sort)and(len(lists)==lens):
   lists=list(lists)
   for i in range(lens):
    if self.data[i]==lists[i]:
     judge=False
     break
  else:judge=False
  return judge
 def __ne__(self,lists):
  lens,judge=len(self),False
  if isinstance(lists,sort)and(len(lists)==lens):
   lists=list(lists)
   for i in range(lens):
    if self.data[i]!=lists[i]:
     judge=True
     break
  else:judge=True
  return judge
 @staticmethod
 def _ascending(item):
  if isinstance(item,(int,float)):return(0,item,'')
  elif isinstance(item,Number):return(0,item.val,'')
  item_str=str(item)
  if item_str.isdigit():return(1,int(item_str),'')
  if item_str.isascii() and item_str.isalpha():return(2,[(i.lower(),0 if i.islower() else 1) for i in item_str])
  if any(i.isdigit() for i in item_str):
   has_ascii,has_japanese=any(i.isascii() for i in item_str),any(ord(i)>127 for i in item_str)
   if has_ascii and not has_japanese:return(3,item_str,'')
   elif has_japanese and has_ascii:return(5,item_str,'')
   return(4,item_str,'')
  if all(ord(i)>127 or i.isspace() for i in item_str):return(4,item_str,'')
  return(5,item_str,'')
 @staticmethod
 def _descending(item):
  if isinstance(item,(int,float)):return(5,item,'')
  if isinstance(item,Number):return(5,item.val,'')
  item_str=str(item)
  if item_str.isdigit():return(4,int(item_str),'')
  if item_str.isascii() and item_str.isalpha():return(3,[(i.lower(),5 if i.islower() else 4) for i in item_str])
  if any(i.isdigit() for i in item_str):
   has_ascii,has_japanese=any(i.isascii() for i in item_str),any(ord(i)>127 for i in item_str)
   if has_ascii and not has_japanese:return(2,item_str,'')
   elif has_japanese and has_ascii:return(0,item_str,'')
   return(1,item_str,'')
  if all(ord(i)>127 or i.isspace() for i in item_str):return(1,item_str,'')
  return(0,item_str,'')
class Number:
 def __init__(self,val):
  if not isinstance(val,(Number,int,float,bool)):
   raise TypeError('valに数値を指定してください')
  if isinstance(val,Number):self.val=val.val
  elif isinstance(val,bool):self.val=int(val)
  else:self.val=val
 @classmethod
 def __instancecheck__(cls,ins):return isinstance(ins,Number)
 def __getattribute__(self,name):return super().__getattribute__(name)
 def __sizeof__(self):return super().__sizeof__()+getsizeof(self.val)
 def __int__(self):return int(self.val)
 def __float__(self):return float(self.val)
 def __str__(self):return str(self.val)
 def __len__(self):return len(str(self.val))
 def len(self):return len(str(self.val))
 def __bool__(self):
  if 0<=self.val:return True
  return False
 def __format__(self,format_spec):return format(self.val,format_spec)
 def format(self,format_spec):return format(self.val,format_spec)
 def types(self):return type(self.val)
 def __add__(self,val):
  self.val=self.val+self._maths_(val)
  return self
 def __sub__(self,val):
  self.val=self.val-self._maths_(val)
  return self
 def __mul__(self,val):
  self.val=self.val*self._maths_(val)
  return self
 def __pow__(self,val):
  self.val=self.val**self._maths_(val)
  return self
 def __ipow__(self,val):
  self.val**=self._maths_(val)
  return self
 def __truediv__(self,val):
  self.val=self.val/self._maths_(val)
  return self
 def __floordiv__(self,val):
  self.val=self.val//self._maths_(val)
  return self
 def __radd__(self,val):
  self.val=self._maths_(val)+self.val
  return self
 def __rsub__(self,val):
  self.val=self._maths_(val)-self.val
  return self
 def __rmul__(self,val):
  self.val=self._maths_(val)*self.val
  return self
 def __rtruediv__(self,val):
  self.val=self._maths_(val)/self.val
  return self
 def __rmod__(self,val):
  self.val=self._maths_(val)%self.val
  return self
 def __rpow__(self,val):
  self.val=self._maths_(val)**self.val
  return self
 def __rfloordiv__(self,val):
  self.val=self._maths_(val)//self.val
  return self
 def __iadd__(self,val):
  self.val+=self._maths_(val)
  return self
 def __isub__(self,val):
  self.val-=self._maths_(val)
  return self
 def __imul__(self,val):
  self.val*=self._maths_(val)
  return self
 def __itruediv__(self,val):
  self.val/=self._maths_(val)
  return self
 def __abs__(self):
  if self.val<0:self.val=abs(self.val)
  return self
 def __eq__(self,val):return self.val==(val.val if isinstance(val,Number) else val)
 def __ne__(self,val):return self.val!=(val.val if isinstance(val,Number) else val)
 def __lt__(self,val):return self.val<self._maths_(val)
 def __le__(self,val):return self.val<=self._maths_(val)
 def __gt__(self,val):return self.val>self._maths_(val)
 def __ge__(self,val):return self.val>=self._maths_(val)
 def __round__(self,n=0):
  self.val=round(self.val,self._maths_(n))
  return self
 def __ceil__(self):
  self.val=ceil(self.val)
  return self
 def __floor__(self):
  self.val=floor(self.val)
  return self
 def __neg__(self):
  self.val=-self.val
  return self
 def __pos__(self):return self
 def _maths_(self,val):
  if isinstance(val,Number):return val.val
  elif isinstance(val,(int,float)):return val
  raise TypeError('数値の型を指定してください')
 def value(self):return self.val