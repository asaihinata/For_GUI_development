'''
色をデータに変換するモジュール

指定できる形式はRGB,HSL,HEX,カラー名のみ

指定できるカラー名はCSSで指定できる色名  https://drafts.csswg.org/css-color-4/#named-colors
'''
__all__=['NPColor']
class NPColor:
 def __init__(self,color):'''色についてセットされたnumpyの配列を作成する。

 :param color: 色名を指定する。
 :type color: str|list[str]|tuple[str]|NDArray[str_]'''
 def __repr__(self)->str:...