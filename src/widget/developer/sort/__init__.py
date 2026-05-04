from ...developer import LIST,Number
class sort:
 def __init__(self,data,types=True):
  if not isinstance(data,list|tuple|LIST):
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
  if isinstance(item,int|float):return(0,item,'')
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
  if isinstance(item,int|float):return(5,item,'')
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