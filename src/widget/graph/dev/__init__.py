from typing import TypeAlias
import japanize_matplotlib
import numpy as np
from matplotlib.pyplot import cm,rcParams
from ..._function import *
from .typing import *
from ..base import polarElement,threeElement,twoElement
from ..base.lists import *
from ..base.style import *
def mod(a:Type_Number,b:Type_Number)->TupleNumbertype2:
 '''整数除算と除算をtuple型で返す。

 :param a: 割られる数を指定する。
 :type a: Type_Number
 :param b: 割る数を指定する。
 :type b: Type_Number
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