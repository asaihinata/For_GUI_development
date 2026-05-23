from datetime import datetime
from numpy import _ArrayT
from typing import IO,Any,overload
from ...base import NPArray
from ..typing import Dtype
__all__=['Formatconversion','strconversions','conversions']
@overload
def strconversions(
formatstr:bytes|str|IO[str]|IO[Any]|None,
year:bool=False,
day:bool=...
)->str:'''様々な日付のフォーマットを特定の日付フォーマットに変換する。

 :param formatstr: 日付の文字列を指定する。
 :type formatstr: bytes|str|IO[str]|IO[Any]|None
 :param year: 曖昧な3桁の整数日付の最初の値を年として判別するか指定する。
 :type year: bool
 :param day: 曖昧な3桁の整数日付の最初の値を日付もしくは月として判別するか指定する。
 :type day: bool
 :return: `datetime`の文字列を返す。
 :rtype: str'''
@overload
def strconversions(
formatstr:bytes|str|IO[str]|IO[Any]|None,
year:bool=False,
day:bool=True
)->str:'''様々な日付のフォーマットを特定の日付フォーマットに変換する。

 :param formatstr: 日付の文字列を指定する。
 :type formatstr: bytes|str|IO[str]|IO[Any]|None
 :param year: 曖昧な3桁の整数日付の最初の値を年として判別するか指定する。
 :type year: bool
 :param day: 曖昧な3桁の整数日付の最初の値を日付として判別するか指定する。
 :type day: bool
 :return: `datetime`の文字列を返す。
 :rtype: str'''
@overload
def strconversions(
formatstr:bytes|str|IO[str]|IO[Any]|None,
year:bool=False,
day:bool=False
)->str:'''様々な日付のフォーマットを特定の日付フォーマットに変換する。

 :param formatstr: 日付の文字列を指定する。
 :type formatstr: bytes|str|IO[str]|IO[Any]|None
 :param year: 曖昧な3桁の整数日付の最初の値を年として判別するか指定する。
 :type year: bool
 :param day: 曖昧な3桁の整数日付の最初の値を月として判別するか指定する。
 :type day: bool
 :return: `datetime`の文字列を返す。
 :rtype: str'''
@overload
def conversions(
formatstr:bytes|str|IO[str]|IO[Any]|None,
year:bool=False,
day:bool=...
)->datetime:'''様々な日付のフォーマットを特定の日付フォーマットに変換する。

 :param formatstr: 日付の文字列を指定する。
 :type formatstr: bytes|str|IO[str]|IO[Any]|None
 :param year: 曖昧な3桁の整数日付の最初の値を年として判別するか指定する。
 :type year: bool
 :param day: 曖昧な3桁の整数日付の最初の値を日付もしくは月として判別するか指定する。
 :type day: bool
 :return: `datetime`の文字列を返す。
 :rtype: datetime'''
@overload
def conversions(
formatstr:bytes|str|IO[str]|IO[Any]|None,
year:bool=False,
day:bool=True
)->datetime:'''様々な日付のフォーマットを特定の日付フォーマットに変換する。

 :param formatstr: 日付の文字列を指定する。
 :type formatstr: bytes|str|IO[str]|IO[Any]|None
 :param year: 曖昧な3桁の整数日付の最初の値を年として判別するか指定する。
 :type year: bool
 :param day: 曖昧な3桁の整数日付の最初の値を日付として判別するか指定する。
 :type day: bool
 :return: `datetime`の文字列を返す。
 :rtype: datetime'''
@overload
def conversions(
formatstr:bytes|str|IO[str]|IO[Any]|None,
year:bool=False,
day:bool=False
)->datetime:'''様々な日付のフォーマットを特定の日付フォーマットに変換する。

 :param formatstr: 日付の文字列を指定する。
 :type formatstr: bytes|str|IO[str]|IO[Any]|None
 :param year: 曖昧な3桁の整数日付の最初の値を年として判別するか指定する。
 :type year: bool
 :param day: 曖昧な3桁の整数日付の最初の値を月として判別するか指定する。
 :type day: bool
 :return: `datetime`の文字列を返す。
 :rtype: datetime'''
class Formatconversion(NPArray):
 def __init__(
self,
data:_ArrayT,
dtype:Dtype|None='datetime64[D]',
yearfirst:bool=...,
dayfirst:bool=...
)->None:...