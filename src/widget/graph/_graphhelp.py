import japanize_matplotlib
import numpy as np
from ...types import *
from .._function import *
from .Graph import threeDElement,twoDElement
from .support.Graphhelp import *
def mod(a:int|float,b:int|float)->TupleNumbertype2:
 '''整数除算と除算をtuple型で返す。

 :param a: 割られる数を指定する。
 :type a: int|float
 :param b: 割る数を指定する。
 :type b: int|float
 :rtype: TupleNumbertype2'''
 return(a//b,a%b)
def datareversed(data:np.ndarray|list|tuple)->np.ndarray|list|tuple:
 '''配列の逆順を返す。

 :param data: 逆順したい配列を指定する。
 :type data: np.ndarray|list|tuple
 :rtype: np.ndarray|list|tuple'''
 if isinstance(data,list):return data.reverse()
 if isinstance(data,tuple|np.ndarray):return data[::-1]
 return data