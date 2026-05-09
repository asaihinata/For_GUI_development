'''閉じられていない線の両端点の描画の方法を指定するモジュール'''
from typing import Literal
__all__:list[str]=['CAPSTYLE_LIST','Capstyle']
CAPSTYLE_LIST:list[str]=['butt','round','projecting']
class Capstyle:
 capstyle_list:list[str]=CAPSTYLE_LIST
 cap:str
 def __init__(self,cap:Literal['butt','round','projecting'])->None:
  '''閉じられていない線の両端点の描画の方法を指定する。

  :param cap: _description_
  :type cap: Literal['butt','round','projecting']
  :raises TypeError: `cap`に文字列以外を指定した場合に発生させる'''
  if not isinstance(cap,str):
   raise TypeError('capにはstr型を指定してください')
  cap=cap.lower()
  if cap in self.capstyle_list:self.cap=cap
  else:self.cap='butt'
 def __str__(self)->str:return self.cap