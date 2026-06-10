'''閉じられていない線の両端点の描画の方法を設定するモジュール'''
from collections.abc import Iterator
from typing import Any, Literal

__all__=['CAPSTYLE_LIST','Capstyle']
class CAPSTYLE_LIST:
 '''capstyleのデータクラス'''
 capstyle_list:list[str]=['butt','round','projecting']
 def __init__(self)->None:pass
 def __iter__(self)->Iterator[str]:return iter(self.capstyle_list)
 def __len__(self)->int:return len(self.capstyle_list)
 def __contains__(self,item:Any)->bool:return item in self.capstyle_list
class Capstyle:
 cap:str
 def __init__(self,cap:Literal['butt','round','projecting'])->None:
  '''閉じられていない線の両端点の描画の方法を指定する。

 :param cap: 閉じられていない線の両端点の描画の方法を指定する。
 :type cap: Literal['butt','round','projecting']
 :raises TypeError: `cap`に文字列以外を指定した場合に発生させる'''
  if not isinstance(cap,str):
   raise TypeError('capにはstr型を指定してください')
  if cap in CAPSTYLE_LIST():self.cap=cap
  else:self.cap='butt'
 def __str__(self)->str:return self.cap