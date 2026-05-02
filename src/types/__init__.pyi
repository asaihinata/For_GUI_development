'''基本的な型ヒント'''
from os import PathLike
from typing import *
from numpy import floating,int_,ndarray,str_
from numpy.typing import NDArray
from matplotlib.typing import *
type StrPathtype=str|PathLike[str]
'''StrPathtype型

フォルダやファイルのパス名の型ヒント'''
Listlike=TypeVar('TypeVar',Sequence[Any])
'''Listlike型

一次元の配列の型'''
type Linktype=str
'''Linktype型

URLのリンクの型ヒント'''
type fontname=str
'''fontname型

フォント名の型ヒント'''
type Numbertype=int|float
'''Numbertype型

int型,float型の型ヒント'''
type Arraytype=list|tuple
'''Arraytype型

list型,tuple型の型ヒント'''
type nArraytype=list|tuple|None
'''Arraytype型

list型,tuple型,Noneの型ヒント'''
type NpArraytype=ndarray|list|tuple
'''NpArraytype型

ndarray型,list型,tuple型の型ヒント'''
type nNpArraytype=ndarray|list|tuple|None
'''nNpArraytype型

ndarray型,list型,tuple型,Noneの型ヒント'''
type TupleNumbertype2=tuple[Numbertype,Numbertype]
'''TupleNumbertype2型

tuple[Numbertype,Numbertype]の型ヒント'''
type TupleNumbertype4=tuple[Numbertype,Numbertype,Numbertype,Numbertype]
'''TupleNumbertype4型

tuple[Numbertype,Numbertype,Numbertype,Numbertype]の型ヒント'''
type TupleInt2=tuple[int,int]
'''TupleInt2型

tuple[int,int]の型ヒント'''
type TupleInt4=tuple[int,int,int,int]
'''TupleInt4型

tuple[int,int,int,int]の型ヒント'''
type TupleFloat2=tuple[float,float]
'''TupleFloat2型

tuple[float,float]の型ヒント'''
type TupleFloat4=tuple[float,float,float,float]
'''TupleFloat4型

tuple[float,float,float,float]の型ヒント'''
type ListNumbertype2=list[Numbertype,Numbertype]
'''ListNumbertype2型

list[Numbertype,Numbertype]の型ヒント'''
type ListNumbertype4=list[Numbertype,Numbertype,Numbertype,Numbertype]
'''ListNumbertype4型

list[Numbertype,Numbertype,Numbertype,Numbertype]の型ヒント'''
type ListInt2=list[int,int]
'''ListInt2型

list[int,int]の型ヒント'''
type ListInt4=list[int,int,int,int]
'''ListInt4型

list[int,int,int,int]の型ヒント'''
type ListFloat2=list[float,float]
'''ListFloat2型

list[float,float]の型ヒント'''
type ListFloat4=list[float,float,float,float]
'''ListFloat4型

list[float,float,float,float]の型ヒント'''
def _f()->None:pass
FunctionType=type(_f)
type labeltype=str|list|tuple|None
'''labeltype型

グラフのラベルに関する型ヒント(str|list|tuple|None)'''
type o_array=list[int,float,str]|tuple[int,float,str]|NDArray[str_]|NDArray[int_]|NDArray[floating]
'''o_array型

一次元配列の`x`,`y`,`z`,`data`の型ヒント'''
type n_array=list|tuple|NDArray
'''n_array型

多次元配列の`x`,`y`,`z`,`data`の型ヒント'''