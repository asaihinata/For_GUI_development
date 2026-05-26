from collections.abc import Sequence
from typing import Iterable,Literal,NoReturn
from matplotlib.axes._axes import Axes
from mpl_toolkits.mplot3d.axes3d import Axes3D
from numpy.typing import ArrayLike
class Xaxis:
 ax:Axes|Axes3D
 def __init__(self,ax:Axes|Axes3D)->None:...
 def FixedLocator(
self,
locs:Sequence[float]|None=None,
nbins:int|None=None
)->None:...
 def LinearLocator(
self,
numticks:int|None=None,
presets:dict[tuple[float,float],Sequence[float]]|None=None
)->None:...
 def MultipleLocator(
self,
base:float=1.0,
offset:float=0.0
)->None:...
 def MaxNLocator(
self,
nbins:int|Literal['auto']=10,
steps:ArrayLike=None,
integer:bool=False,
symmetric:bool=False,
prune:Literal['lower','upper','both']|None=None,
min_n_ticks:int=2
)->None:...
 def set_log(
self,
base:float|int=10,
nonpositive:Literal['clip','mask']='clip',
subs:Iterable[int]|None=None
):'''対数スケールを作成する。

 :param base: 対数の底を指定する。
 :type base: float|int
 :param nonpositive: 非正の値に対する動作を指定する。
 :type nonpositive: Literal['clip','mask']
 :param subs: 各主目盛りの間にサブ目盛りを配置する場所を指定する。
 :type subs: Iterable[int]|None
 :return:
 :rtype: NoReturn'''
class Yaxis:
 ax:Axes|Axes3D
 def __init__(self,ax:Axes|Axes3D)->None:...
 def FixedLocator(
self,
locs:Sequence[float]|None=None,
nbins:int|None=None
)->None:...
 def LinearLocator(
self,
numticks:int|None=None,
presets:dict[tuple[float,float],Sequence[float]]|None=None
)->None:...
 def MultipleLocator(
self,
base:float=1.0,
offset:float=0.0
)->None:...
 def MaxNLocator(
self,
nbins:int|Literal['auto']=10,
steps:ArrayLike=None,
integer:bool=False,
symmetric:bool=False,
prune:Literal['lower','upper','both']|None=None,
min_n_ticks:int=2
)->None:...
 def set_log(
self,
base:float|int=10,
nonpositive:Literal['clip','mask']='clip',
subs:Iterable[int]|None=None
):'''対数スケールを作成する。

 :param base: 対数の底を指定する。
 :type base: float|int
 :param nonpositive: 非正の値に対する動作を指定する。
 :type nonpositive: Literal['clip','mask']
 :param subs: 各主目盛りの間にサブ目盛りを配置する場所を指定する。
 :type subs: Iterable[int]|None
 :return:
 :rtype: NoReturn'''
class Zaxis:
 ax:Axes3D
 def __init__(self,ax:Axes3D)->None:...
 def FixedLocator(
self,
locs:Sequence[float]|None=None,
nbins:int|None=None
)->None:...
 def LinearLocator(
self,
numticks:int|None=None,
presets:dict[tuple[float,float],Sequence[float]]|None=None
)->None:...
 def MultipleLocator(
self,
base:float=1.0,
offset:float=0.0
)->None:...
 def MaxNLocator(
self,
nbins:int|Literal['auto']=10,
steps:ArrayLike=None,
integer:bool=False,
symmetric:bool=False,
prune:Literal['lower','upper','both']|None=None,
min_n_ticks:int=2
)->None:...
 def set_log(
self,
base:float|int=10,
nonpositive:Literal['clip','mask']='clip',
subs:Iterable[int]|None=None
):'''対数スケールを作成する。

 :param base: 対数の底を指定する。
 :type base: float|int
 :param nonpositive: 非正の値に対する動作を指定する。
 :type nonpositive: Literal['clip','mask']
 :param subs: 各主目盛りの間にサブ目盛りを配置する場所を指定する。
 :type subs: Iterable[int]|None
 :return:
 :rtype: NoReturn'''