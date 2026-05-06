from ...developer import LIST
from .Number import Number
__all__=['LISTNumber']
class LISTNumber:
 def __init__(self,obj):
  if not isinstance(obj,list|LIST|tuple):
   raise TypeError('型によるエラー')
  self.lists=[i.val if isinstance(i,Number) else i for i in obj]
  self.judge=all(isinstance(i,int|float)for i in self.lists)
 def __bool__(self):return self.judge
 def __iter__(self):return iter(self.lists)
 def __len__(self):return len(self.lists)
 def __contains__(self,item):return item in self.lists