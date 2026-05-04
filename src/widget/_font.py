from tkinter import Misc,Tk
from tkinter.font import Font,families
from ..typing import Literal
from ._function import bols,listchose,nums
__all__=['fonts']
class fonts(Font):
 def __init__(
self,
family:str='Meiryo',
size:int|float=14,
weight:Literal['normal','bold']='normal',
slant:Literal['roman','italic']='roman',
underline:bool=False,
overstrike:bool=False,
root:Misc=None
)->None:
  '''フォントに関するクラス

 :param family: フォント名を指定する。
 :type family: str
 :param size: フォントサイズを指定する。
 :type size: int|float
 :param weight: フォントの太字を指定する。
 :type weight: Literal['normal','bold']
 :param slant: フォントの斜体を指定する。
 :type slant: Literal['roman','italic']
 :param underline: フォントに下線を付けるか指定する。
 :type underline: bool
 :param overstrike: フォントに取り消し線を付けるか指定する。
 :type overstrike: bool'''
  self.rootj,self.root=False,root
  if not isinstance(self.root,Misc):self.root,self.rootj=Tk(),True
  self.fontlist=families(self.root)
  self.family=family if family in self.fontlist else self.fontlist[0]
  if self.rootj:self.root.destroy()
  self.size=nums(size,14)
  self.weight=listchose(weight,['normal','bold'])
  self.slant=listchose(slant,['roman','italic'])
  self.underline=bols(underline,False)
  self.overstrike=bols(overstrike,False)
  super().__init__(family=self.family,size=self.size,weight=self.weight,slant=self.slant,underline=self.underline,overstrike=self.overstrike,root=self.root)