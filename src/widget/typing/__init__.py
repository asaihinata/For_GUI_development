'''フレームワーク全体で使用する型'''
from collections.abc import Iterable
from typing import Any,Callable,Collection,Literal,NoReturn,TypeAlias,TypeVar,overload
import numpy as np
from matplotlib.typing import ColorType
from numpy.typing import NDArray
__all__=['Any','Callable','Collection','ColorType','ColorTypes','FunctionType','Iterable','labeltype','Literal','NoReturn','overload','ListFloat2','ListFloat4','ListInt2','ListInt4','ListNumbertype2','ListNumbertype4','TupleFloat2','TupleFloat4','TupleInt2','TupleInt4','TupleNumbertype2','TupleNumbertype4','Type_Iterableint','Type_Iterablestr','Type_Number','Type_Numberlike','_T','n_array','o_array']
_T=TypeVar('_T')
# Iterable
Type_Iterablestr:TypeAlias=Iterable[str]
Type_Iterableint:TypeAlias=Iterable[int]
# number
Type_Number:TypeAlias=int|float
Type_Numberlike:TypeAlias=bool|np.bool|int|float|np.float16|np.float32|np.float64|np.int16|np.int32|np.int64|np.int8|np.uint16|np.uint32|np.uint64|np.uint8
# list like and number type
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
# Graph
labeltype:TypeAlias=str|list|tuple|None
o_array:TypeAlias=list[int,float,str]|tuple[int,float,str]|NDArray[np.str_]|NDArray[np.int_]|NDArray[np.floating]
n_array:TypeAlias=list|tuple|NDArray
ColorTypes:TypeAlias=ColorType|None