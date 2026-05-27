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
class _Arry:
 arr:np.ndarray
 dt:DTypeLike
 def __init__(
self,
arr:np.ndarray
):''':raises TypeError: `arr`にnp.ndarray以外の型を指定した場合に発生させる'''
class integerDtype(_Arry):
 def __init__(
self,
arr:np.ndarray
):''':raises TypeError: `arr`にnp.ndarray以外の型を指定した場合に発生させる'''
 @property
 def bool(self)->bool:'''`arr`のdtypeの型が`np.integer`なのか判定する。'''
 def __bool__(self)->bool:'''`arr`のdtypeの型が`np.integer`なのか判定する。'''
class intDtype(_Arry):
 def __init__(
self,
arr:np.ndarray
):''':raises TypeError: `arr`にnp.ndarray以外の型を指定した場合に発生させる'''
 @property
 def bool(self)->bool:'''`arr`のdtypeの型が`np.int_`なのか判定する。'''
 def __bool__(self)->bool:'''`arr`のdtypeの型が`np.int_`なのか判定する。'''
class uintDtype(_Arry):
 def __init__(
self,
arr:np.ndarray
):''':raises TypeError: `arr`にnp.ndarray以外の型を指定した場合に発生させる'''
 @property
 def bool(self)->bool:'''`arr`のdtypeの型が`np.uint`なのか判定する。'''
 def __bool__(self)->bool:'''`arr`のdtypeの型が`np.uint`なのか判定する。'''
class floatDtype(_Arry):
 def __init__(
self,
arr:np.ndarray
):''':raises TypeError: `arr`にnp.ndarray以外の型を指定した場合に発生させる'''
 @property
 def bool(self)->bool:'''`arr`のdtypeの型が`np.floating`なのか判定する。'''
 def __bool__(self)->bool:'''`arr`のdtypeの型が`np.floating`なのか判定する。'''
class boolDtype(_Arry):
 def __init__(
self,
arr:np.ndarray
):''':raises TypeError: `arr`にnp.ndarray以外の型を指定した場合に発生させる'''
 @property
 def bool(self)->bool:'''`arr`のdtypeの型が`np.bool_`なのか判定する。'''
 def __bool__(self)->bool:'''`arr`のdtypeの型が`np.bool_`なのか判定する。'''
class complexDtype(_Arry):
 def __init__(
self,
arr:np.ndarray
):''':raises TypeError: `arr`にnp.ndarray以外の型を指定した場合に発生させる'''
 @property
 def bool(self)->bool:'''`arr`のdtypeの型が`np.complexfloating`なのか判定する。'''
 def __bool__(self)->bool:'''`arr`のdtypeの型が`np.complexfloating`なのか判定する。'''
class strDtype(_Arry):
 def __init__(
self,
arr:np.ndarray
):''':raises TypeError: `arr`にnp.ndarray以外の型を指定した場合に発生させる'''
 @property
 def bool(self)->bool:'''`arr`のdtypeの型が`np.str_`なのか判定する。'''
 def __bool__(self)->bool:'''`arr`のdtypeの型が`np.str_`なのか判定する。'''
class bytesDtype(_Arry):
 def __init__(
self,
arr:np.ndarray
):''':raises TypeError: `arr`にnp.ndarray以外の型を指定した場合に発生させる'''
 @property
 def bool(self)->bool:'''`arr`のdtypeの型が`np.bytes_`なのか判定する。'''
 def __bool__(self)->bool:'''`arr`のdtypeの型が`np.bytes_`なのか判定する。'''
class datetimeDtype(_Arry):
 def __init__(
self,
arr:np.ndarray
):''':raises TypeError: `arr`にnp.ndarray以外の型を指定した場合に発生させる'''
 @property
 def bool(self)->bool:'''`arr`のdtypeの型が`np.datetime64`なのか判定する。'''
 def __bool__(self)->bool:'''`arr`のdtypeの型が`np.datetime64`なのか判定する。'''
class timedeltaDtype(_Arry):
 def __init__(
self,
arr:np.ndarray
):''':raises TypeError: `arr`にnp.ndarray以外の型を指定した場合に発生させる'''
 @property
 def bool(self)->bool:'''`arr`のdtypeの型が`np.timedelta64`なのか判定する。'''
 def __bool__(self)->bool:'''`arr`のdtypeの型が`np.timedelta64`なのか判定する。'''