import japanize_matplotlib
import numpy as np
from ...types import *
from .._function import *
from .Graph import threeDElement,twoDElement
from .support.Graphhelp import *
def mod(a:Numbertype,b:Numbertype)->TupleNumbertype2:
 '''整数除算と除算をtuple型で返す。

 :param a: 割られる数を指定する。
 :type a: Numbertype
 :param b: 割る数を指定する。
 :type b: Numbertype
 :rtype: TupleNumbertype2'''
 return(a//b,a%b)
def datareversed(data:NpArraytype)->NpArraytype:
 '''配列の逆順を返す。

 :param data: 逆順したい配列を指定する。
 :type data: NpArraytype
 :rtype: NpArraytype'''
 if isinstance(data,list):return data.reverse()
 if isinstance(data,tuple|np.ndarray):return data[::-1]
 return data