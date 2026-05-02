from os import PathLike
from typing import Any,TypeAlias,Callable,Literal,NoReturn,Sequence,TypeVar
from numpy import floating,int_,ndarray,str_
from numpy.typing import NDArray
from matplotlib.typing import ColorType
# str type
type StrPathtype=str|PathLike[str]
StrPathtype=(str,PathLike)
type Linktype=str
Linktype=str
type fontname=str
fontname=str
# number type
type Numbertype=int|float
Numbertype=(int,float)
# list like type
type Arraytype=list|tuple
Arraytype=(list,tuple)
type nArraytype=list|tuple|None
nArraytype=(list,tuple,None)
type NpArraytype=ndarray|list|tuple
NpArraytype=(ndarray,list,tuple)
type nNpArraytype=ndarray|list|tuple|None
nNpArraytype=(ndarray,list,tuple,None)
Listlike=TypeVar('Listlike',bound=Sequence[Any])
# list like and number type
type TupleNumbertype2=tuple[Numbertype,Numbertype]
type TupleNumbertype4=tuple[Numbertype,Numbertype,Numbertype,Numbertype]
type TupleInt2=tuple[int,int]
type TupleInt4=tuple[int,int,int,int]
type TupleFloat2=tuple[float,float]
type TupleFloat4=tuple[float,float,float,float]
type ListNumbertype2=list[Numbertype,Numbertype]
type ListNumbertype4=list[Numbertype,Numbertype,Numbertype,Numbertype]
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