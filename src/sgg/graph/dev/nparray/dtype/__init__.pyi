from typing import Literal
import numpy as np
from numpy._typing import DTypeLike
__all__=[
'boolDtype',
'bytesDtype',
'complexDtype',
'datetimeDtype',
'floatDtype',
'intDtype',
'integerDtype',
'strDtype',
'timedeltaDtype',
'uintDtype'
]
class Arry:
 arr:np.ndarray
 dt:DTypeLike
 def __init__(
self,
arr:np.ndarray,
dtype:np.integer|np.int_|np.uint|np.floating|np.bool_|np.complexfloating|np.str_|np.bytes_|np.datetime64|np.timedelta64
):''':raises TypeError: `arr`にnp.ndarray以外の型を指定した場合に発生させる'''
class integerDtype(Arry):
 def __init__(
self,
arr:np.ndarray
):''':raises TypeError: `arr`にnp.ndarray以外の型を指定した場合に発生させる'''
 def __bool__(self)->bool:'''`arr`のdtypeの型が`np.integer`なのか判定する。'''
class intDtype(Arry):
 def __init__(
self,
arr:np.ndarray
):''':raises TypeError: `arr`にnp.ndarray以外の型を指定した場合に発生させる'''
 def __bool__(self)->bool:'''`arr`のdtypeの型が`np.int_`なのか判定する。'''
class uintDtype(Arry):
 def __init__(
self,
arr:np.ndarray
):''':raises TypeError: `arr`にnp.ndarray以外の型を指定した場合に発生させる'''
 def __bool__(self)->bool:'''`arr`のdtypeの型が`np.uint`なのか判定する。'''
class floatDtype(Arry):
 def __init__(
self,
arr:np.ndarray
):''':raises TypeError: `arr`にnp.ndarray以外の型を指定した場合に発生させる'''
 def __bool__(self)->bool:'''`arr`のdtypeの型が`np.floating`なのか判定する。'''
class boolDtype(Arry):
 def __init__(
self,
arr:np.ndarray
):''':raises TypeError: `arr`にnp.ndarray以外の型を指定した場合に発生させる'''
 def __bool__(self)->bool:'''`arr`のdtypeの型が`np.bool_`なのか判定する。'''
class complexDtype(Arry):
 def __init__(
self,
arr:np.ndarray
):''':raises TypeError: `arr`にnp.ndarray以外の型を指定した場合に発生させる'''
 def __bool__(self)->bool:'''`arr`のdtypeの型が`np.complexfloating`なのか判定する。'''
class strDtype(Arry):
 def __init__(
self,
arr:np.ndarray
):''':raises TypeError: `arr`にnp.ndarray以外の型を指定した場合に発生させる'''
 def __bool__(self)->bool:'''`arr`のdtypeの型が`np.str_`なのか判定する。'''
class bytesDtype(Arry):
 def __init__(
self,
arr:np.ndarray
):''':raises TypeError: `arr`にnp.ndarray以外の型を指定した場合に発生させる'''
 def __bool__(self)->bool:'''`arr`のdtypeの型が`np.bytes_`なのか判定する。'''
class datetimeDtype(Arry):
 def __init__(
self,
arr:np.ndarray
):''':raises TypeError: `arr`にnp.ndarray以外の型を指定した場合に発生させる'''
 def __bool__(self)->bool:'''`arr`のdtypeの型が`np.datetime64`なのか判定する。'''
class timedeltaDtype(Arry):
 def __init__(
self,
arr:np.ndarray
):''':raises TypeError: `arr`にnp.ndarray以外の型を指定した場合に発生させる'''
 def __bool__(self)->bool:'''`arr`のdtypeの型が`np.timedelta64`なのか判定する。'''