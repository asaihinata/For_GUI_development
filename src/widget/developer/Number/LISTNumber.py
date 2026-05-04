from ..LIST import LIST
from .Number import Number
class LISTNumber:
 def __init__(self,obj):
  if not isinstance(obj,list|LIST|tuple):
   raise TypeError('型によるエラー')
  self.lists=obj
  self.judge=all(isinstance(i,int|float|Number)for i in self.lists)
 def __bool__(self):return self.judge
 def __iter__(self):return iter([i.val if isinstance(i,Number) else i for i in self.lists])
 def __len__(self):return len(self.lists)