from _collections_abc import dict_items
from matplotlib import RcParams
from ....types import Any,Literal,Numbertype,fontname,overload
class pltFont:
 variantlist:list
 stretchlist:list
 weightlist:list
 sizelist:list
 stylelist:list
 rcparams:RcParams
 family:fontname
 size:Numbertype|str
 stretch:Numbertype|str
 weight:Numbertype|str
 style:str
 variant:str
 def __init__(
self,
family:fontname='sans-serif',
size:Numbertype|Literal['xx-small','x-small','small','medium','large','x-large','xx-large']=10,
stretch:Numbertype|Literal['ultra-condensed','extra-condensed','condensed','semi-condensed','normal','semi-expanded','expanded','extra-expanded','ultra-expanded']='normal',
style:Literal['normal','italic','oblique']='normal',
variant:Literal['normal','small-caps']='normal',
weight:Numbertype|Literal['ultralight','light','normal','regular','book','medium','roman','semibold','demibold','demi','bold','heavy','extra bold','black']='normal'
)->None:'''グラフのフォントを指定する。

 :param family: _description_
 :type family: fontname
 :param size: _description_
 :type size: Numbertype
 :param stretch: _description_
 :type stretch: Numbertype|Literal['ultra-condensed','extra-condensed','condensed','semi-condensed','normal','semi-expanded','expanded','extra-expanded','ultra-expanded']
 :param style: _description_
 :type style: Literal['normal','italic','oblique']
 :param variant: _description_
 :type variant: Literal['normal','small-caps']
 :param weight: _description_
 :type weight: Numbertype|Literal['ultralight','light','normal','regular','book','medium','roman','semibold','demibold','demi','bold','heavy','extra bold','black']'''
 @overload
 def familylist(self)->list[str]:'''現在システムにインストールされており,尚且つ`matplotlib`が認識できるフォント名の一覧を取得する。

 :return: 現在システムにインストールされており,尚且つ`matplotlib`が認識できるフォント名の一覧を配列で返す。
 :rtype: list[str]'''
 @overload
 @staticmethod
 def familylist()->list[str]:'''現在システムにインストールされており,尚且つ`matplotlib`が認識できるフォント名の一覧を取得する。

 :return: 現在システムにインストールされており,尚且つ`matplotlib`が認識できるフォント名の一覧を配列で返す。
 :rtype: list[str]'''
 @overload
 def familys(self)->list[str]:'''システムにインストールされているフォントファイルのパスを取得する。

 :return: システムにインストールされているフォントファイルのパスを取得する。
 :rtype: list[str]'''
 @overload
 @staticmethod
 def familys()->list[str]:'''システムにインストールされているフォントファイルのパスを取得する。

 :return: システムにインストールされているフォントファイルのパスを取得する。
 :rtype: list[str]'''
 def items(self)->dict_items[str,Any]:...
 def __getitem__(self,key:str)->Any:...
 @classmethod
 def __instancecheck__(cls,ins:Any)->bool:...