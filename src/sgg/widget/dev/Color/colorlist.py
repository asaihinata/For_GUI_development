from .data import getcsv
__all__=['ColorData']
class ColorData:
 colorlist=getcsv()
 lens=len(colorlist)
 def __eq__(self,color):return self.colorlist==color
 def __ne__(self,color):return self.colorlist!=color
 def __iter__(self):return iter(self.colorlist)
 def __contains__(self,item):return item in self.colorlist
 def __len__(self):return self.lens
 def __getattribute__(self,name):return super().__getattribute__(name)
 def __getitem__(self,key):
  if isinstance(key,int):
   if 0<=key<self.lens:return self.colorlist[key]
   raise IndexError('配列の範囲外です')
  elif isinstance(key,slice):return self.colorlist[key]
  raise TypeError('keyはintまたはslicesである必要があります')