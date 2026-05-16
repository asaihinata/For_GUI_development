'''塗りつぶし領域の領域内のマーカーを設定するモジュール'''
from re import fullmatch
from ...typing import Type_all
__all__:Type_all=['Hatch','HATCH_DICT','HATCH_LIST']
HATCH_LIST:list[str]=['/','\\','|','-','+','x','o','O','.','*']
HATCH_DICT:dict[str,str]={
'/':'diagonal hatching',
'\\':'back diagonal',
'|':'vertical',
'-':'horizontal',
'+':'crossed',
'x':'crossed diagonal',
'o':'small circle',
'O':'large circle',
'.':'dots',
'*':'stars'
}
class Hatch:
 hatch:str
 def __init__(self,hatch:str)->None:
  '''塗りつぶし領域の領域内のマーカーを作成する。

 :param hatch: 領域内のマーカーを指定する。
 :type hatch: str
 :raises ValueError: `hatch`に`HATCH_LIST`の要素以外の値以外を指定した場合に発生させる'''
  if not fullmatch(r'^[/\\|\-+xo*O.]+$',hatch):
   raise ValueError('HATCH_LISTの要素以外の値が含まれています')
  self.hatch=hatch
 def __str__(self)->str:return self.hatch