"""
GUI全体で使用する型
"""
from typing import Any,Callable,Literal,NoReturn,Sequence,TypeAlias,TypeVar
from matplotlib.typing import ColorType
from numpy import floating,int_,ndarray,str_
from numpy.typing import NDArray
# list like and number type
TupleNumbertype2:TypeAlias=tuple[int|float,int|float]
TupleNumbertype4:TypeAlias=tuple[int|float,int|float,int|float,int|float]
TupleInt2:TypeAlias=tuple[int,int]
TupleInt4:TypeAlias=tuple[int,int,int,int]
TupleFloat2:TypeAlias=tuple[float,float]
TupleFloat4:TypeAlias=tuple[float,float,float,float]
ListNumbertype2:TypeAlias=list[int|float,int|float]
ListNumbertype4:TypeAlias=list[int|float,int|float,int|float,int|float]
ListInt2:TypeAlias=list[int,int]
ListInt4:TypeAlias=list[int,int,int,int]
ListFloat2:TypeAlias=list[float,float]
ListFloat4:TypeAlias=list[float,float,float,float]
# function type
def _f():pass
FunctionType=type(_f)
# graph type
labeltype:TypeAlias=str|list|tuple|None
o_array:TypeAlias=list[int,float,str]|tuple[int,float,str]|NDArray[str_]|NDArray[int_]|NDArray[floating]
n_array:TypeAlias=list|tuple|NDArray