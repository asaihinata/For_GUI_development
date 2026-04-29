from typing import Iterable,Literal,NoReturn
from matplotlib.axes._axes import Axes
from mpl_toolkits.mplot3d.axes3d import Axes3D
class Xaxis:
 ax:Axes
 def __init__(self,ax:Axes)->None:...
 def set_log(
self,
base:float|int=10,
nonpositive:Literal['clip','mask']='clip',
subs:Iterable[int]|None=None
)->NoReturn:'''対数スケールを作成する。

 :param base: 対数の底を指定する。
 :type base: float|int
 :param nonpositive: 非正の値に対する動作を指定する。
 :type nonpositive: Literal['clip','mask']
 :param subs: 各主目盛りの間にサブ目盛りを配置する場所を指定する。
 :type subs: Iterable[int]|None
 :return:
 :rtype: NoReturn'''
class Yaxis:
 ax:Axes
 def __init__(self,ax:Axes)->None:...
 def set_log(
self,
base:float|int=10,
nonpositive:Literal['clip','mask']='clip',
subs:Iterable[int]|None=None
)->NoReturn:'''対数スケールを作成する。

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
 def set_log(
self,
base:float|int=10,
nonpositive:Literal['clip','mask']='clip',
subs:Iterable[int]|None=None
)->NoReturn:'''対数スケールを作成する。

 :param base: 対数の底を指定する。
 :type base: float|int
 :param nonpositive: 非正の値に対する動作を指定する。
 :type nonpositive: Literal['clip','mask']
 :param subs: 各主目盛りの間にサブ目盛りを配置する場所を指定する。
 :type subs: Iterable[int]|None
 :return:
 :rtype: NoReturn'''