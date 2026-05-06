from os import PathLike
from typing import (Any,Callable,Literal,NoReturn,Sequence,TypeAlias,
                    TypeVar)
from matplotlib.typing import ColorType
from numpy import floating,int_,ndarray,str_
from numpy.typing import NDArray
# str type
type StrPathtype=str|PathLike[str]
StrPathtype=(str,PathLike)
# list like and number type
type TupleNumbertype2=tuple[int|float,int|float]
type TupleNumbertype4=tuple[int|float,int|float,int|float,int|float]
type TupleInt2=tuple[int,int]
type TupleInt4=tuple[int,int,int,int]
type TupleFloat2=tuple[float,float]
type TupleFloat4=tuple[float,float,float,float]
type ListNumbertype2=list[int|float,int|float]
type ListNumbertype4=list[int|float,int|float,int|float,int|float]
type ListInt2=list[int,int]
type ListInt4=list[int,int,int,int]
type ListFloat2=list[float,float]
type ListFloat4=list[float,float,float,float]
# function type
def _f():pass
FunctionType=type(_f)
# graph type
type labeltype=str|list|tuple|None
type o_array=list[int,float,str]|tuple[int,float,str]|NDArray[str_]|NDArray[int_]|NDArray[floating]
type n_array=list|tuple|NDArray