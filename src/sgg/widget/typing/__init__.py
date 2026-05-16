'''フレームワーク全体で使用する型を設定しているモジュール'''
from collections.abc import Iterable
from typing import Any,Callable,Collection,Literal,NoReturn,TypeAlias,TypeVar,overload
import numpy as np
from numpy import _ArrayT
from numpy.typing import ArrayLike,NDArray
Type_all:TypeAlias=list[str]
__all__:Type_all=['_ArrayT','_T','Any','ArrayLike','Callable','Collection','ColorType','ColorTypeN','FunctionType','labeltype','ListFloat2','ListFloat4','ListInt2','ListInt4','Listlike','ListNumbertype2','ListNumbertype4','Literal','n_array','nListlike','NoReturn','NPstr2','o_array','overload','RGBAColorType','RGBColorType','TupleFloat2','TupleFloat4','TupleInt2','TupleInt4','TupleNumbertype2','TupleNumbertype4','Type_all','Type_bool','Type_dtype','Type_Iterableint','Type_Iterablestr','Type_npComplex','Type_npComplexs','Type_npFloat','Type_npFloats','Type_npInt','Type_npInts','Type_npUint','Type_Numberlike','Type_NumberlikeN','TypeAlias']
_T=TypeVar('_T')
# Iterable
Type_Iterablestr:TypeAlias=Iterable[str]
Type_Iterableint:TypeAlias=Iterable[int]
# number
Type_npInt:TypeAlias=np.int8|np.int16|np.int32|np.int64
Type_npInts:TypeAlias=int|Type_npInt
Type_npFloat:TypeAlias=np.float16|np.float32|np.float64|np.float96|np.float128
Type_npFloats:TypeAlias=float|Type_npFloat
Type_npUint:TypeAlias=np.uint8|np.uint16|np.uint32|np.uint64
Type_npComplex:TypeAlias=np.complex64|np.complex128|np.complex192|np.complex256
Type_npComplexs:TypeAlias=complex|Type_npComplex
Type_Numberlike:TypeAlias=Type_npComplexs|Type_npUint|Type_npFloats|Type_npInts
Type_NumberlikeN:TypeAlias=Type_Numberlike|None
# numpy
Type_dtype:TypeAlias=np._DTypeT_co|None
# list like and numpy list
Listlike:TypeAlias=list|tuple
nListlike:TypeAlias=np.ndarray|Listlike
NPstr2:TypeAlias=np.ndarray[str,str]|np.ndarray[np.str_,np.str_]
TupleNumbertype2:TypeAlias=tuple[Type_Numberlike,Type_Numberlike]
TupleNumbertype4:TypeAlias=tuple[Type_Numberlike,Type_Numberlike,Type_Numberlike,Type_Numberlike]
TupleInt2:TypeAlias=tuple[int,int]
TupleInt4:TypeAlias=tuple[int,int,int,int]
TupleFloat2:TypeAlias=tuple[float,float]
TupleFloat4:TypeAlias=tuple[float,float,float,float]
ListNumbertype2:TypeAlias=list[Type_Numberlike,Type_Numberlike]
ListNumbertype4:TypeAlias=list[Type_Numberlike,Type_Numberlike,Type_Numberlike,Type_Numberlike]
ListInt2:TypeAlias=list[int,int]
ListInt4:TypeAlias=list[int,int,int,int]
ListFloat2:TypeAlias=list[float,float]
ListFloat4:TypeAlias=list[float,float,float,float]
# function type
def _f():pass
FunctionType=type(_f)
# bool
Type_bool:TypeAlias=bool|np.bool
# Graph
labeltype:TypeAlias=str|list|tuple|None
o_array:TypeAlias=list[int,float,str]|tuple[int,float,str]|NDArray[np.str_]|NDArray[np.int_]|NDArray[np.floating]
n_array:TypeAlias=list|tuple|NDArray
# Color
RGBColorType:TypeAlias=str|tuple[float,float,float]
RGBAColorType:TypeAlias=(
str|
TupleFloat4|
tuple[RGBColorType,float]|
tuple[TupleFloat4,float]
)
ColorType:TypeAlias=RGBColorType|RGBAColorType
ColorTypeN:TypeAlias=ColorType|None