import numpy as np
__all__=['LIST']
class LIST:
 def __init__(self,lists,*arg):
  if isinstance(lists,list):self.lists=lists
  elif isinstance(lists,(tuple,range)):self.lists=list(lists)
  elif isinstance(lists,LIST):self.lists=lists.lists
  elif isinstance(lists,np.ndarray):self.lists=lists.tolist()
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
  if isinstance(val,int):
   if 0<=val<len(self):return self.lists[val]
   raise IndexError('配列の範囲外です')
  elif isinstance(val,slice):return self.lists[val]
  raise TypeError('リストのインデックスはintまたはslicesである必要があります')
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
  elif isinstance(val,list|tuple):
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
  elif isinstance(val,range|list|tuple):
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
  self.lists=sorted(self.lists,key=_ascending if type else _descending)
  return self
 def count(self,val):return self.lists.count(val)
 def empty(self):return self.lists==[]
 @classmethod
 def range(cls,start=0,end=None,step=1,endpoint=False):
  if not isinstance(start,int):
   raise TypeError('startには整数の型を指定してください')
  if not isinstance(step,int):
   raise TypeError('stepには整数の型を指定してください')
  if not isinstance(end,int):end,start=start,0
  if not isinstance(endpoint,bool):endpoint=False
  return LIST(lists=range(start,end+int(endpoint),step))
 @classmethod
 def full(cls,val,size=None):
  if(
   (
    isinstance(size,int) and 1<=size
   ) or
   (
    isinstance(size,list|tuple) and
    all((isinstance(i,int) and 1<=i)for i in size)
   ) or
   (
    isinstance(size,LIST) and
    all((isinstance(i,int) and 1<=i)for i in size)
   )
   ):return LIST(np.full(size,val))
  return LIST(np.full(1,val))
def _ascending(item):
 if isinstance(item,int|float):return(0,item,'')
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
def _descending(item):
 if isinstance(item,int|float):return(5,item,'')
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