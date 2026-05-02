from typing import Any
from .....developer import Number
__all__=['list2float','num0','num0s','num1s']
def num1s(val:int|float|Number=0,mins:int|float|Number=1)->int|float|Number:
 '''`val`が1以上の数値かを調べる。

 :param val: 調べたい数値を指定する。
 :type val: int|float|Number
 :param mins: 調べたい数値`val`の最低値を指定する。
 :type mins: int|float|Number
 :return: 数値を返す。
 :rtype: int|float|Number'''
def num0s(val:int|float|Number=0,mins:int|float|Number=0)->int|float|Number:
 '''`val`が0以上の数値かを調べる。

 :param val: 調べたい数値を指定する。
 :type val: int|float|Number
 :param mins: 調べたい数値`val`の最低値を指定する。
 :type mins: int|float|Number
 :return: 数値を返す。
 :rtype: int|float|Number'''
def num0(val:int|float|Number=0,mins:int|float|Number=0)->int|float|Number:
 '''`val`が0より大きい数値かを調べる。

 :param val: 調べたい数値を指定する。
 :type val: int|float|Number
 :param mins: 調べたい数値`val`の最低値を指定する。
 :type mins: int|float|Number
 :return: 数値を返す。
 :rtype: int|float|Number'''
def list2float(lin:list[Any]|tuple[Any]=None)->bool:...