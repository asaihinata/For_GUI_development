'''
色をデータに変換するモジュール

指定できる形式はRGB,HSL,HEX,カラー名のみ

指定できるカラー名はCSSで指定できる色名  https://drafts.csswg.org/css-color-4/#named-colors
'''
from numpy import ndarray,str_
from numpy.typing import NDArray
__all__=['NPColor']
class NPColor:
 data:ndarray
 def __init__(self,color:str|list[str]|tuple[str]|NDArray[str_]):
  '''色についてセットされたnumpyの配列を作成する。

 :param color: 色名を指定する。
 :type color: str|list[str]|tuple[str]|NDArray[str_]
 :raises TypeError: `color`で配列を指定した際,その配列内の要素に文字列以外の型が含まれているときに発生させる
 :raises TypeError: `color`の型が配列の型もしくはstr型ではない時に発生させる'''
 def __repr__(self)->str:...
 def get_hex_list(self)->ndarray:'''NPColor内の16進数の色コードを取得する。'''
 def get_rgb_list(self)->ndarray:'''NPColor内のRGBを取得する。'''
 def get_r_list(self)->ndarray:'''NPColor内のRGBのRを取得する。'''
 def get_g_list(self)->ndarray:'''NPColor内のRGBのGを取得する。'''
 def get_b_list(self)->ndarray:'''NPColor内のRGBのBを取得する。'''