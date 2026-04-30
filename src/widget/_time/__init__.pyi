from collections.abc import Iterator
import datetime
import time
from typing import Any,NoReturn,overload
from ...types import Listlike
__all__=['times','timeslist']
class times:
 maxsyear:int
 minsyear:int
 year:int
 month:int
 day:int
 hour:int
 minute:int
 second:int
 microsecond:int
 datetimes:datetime.datetime|datetime.date
 @overload
 def __init__(
self,
year:int,
month:int,
day:int,
hour:int=0,
minute:int=0,
second:int=0,
microsecond:int=0,
timezone:datetime._TzInfo='Asia/Tokyo',
fold:int|bool=0
)->None:'''日付と時間を作成するクラス

`year`,`month`,`day`の引数は必須である。int型で指定されている引数にint型以外を指定するとTypeErrorを発生させる。範囲を指定されている引数に範囲外を指定するとValueErrorを発生させる。

 :param year: 年を指定する。範囲は`times.maxsyear<=year<=times.minsyear`
 :type year: int
 :param month: 月を指定する。範囲は`1<=month<=12`
 :type month: int
 :param day: 日にちを指定する。範囲は`1<=day<=指定された年と月の日数`
 :type day: int
 :param hour: 時間を指定する。範囲は`0<=hour<=24`
 :type hour: int
 :param minute: 分を指定する。範囲は`0<=minute<=60`
 :type minute: int
 :param second: 秒を指定する。範囲は`0<=second<=60`
 :type second: int
 :param microsecond: ミリ秒を指定する。範囲は`0<=microsecond<=1000000`
 :type microsecond: int
 :param timezone: タイムゾーンを指定する。
 :type timezone: datetime._TzInfo
 :param fold: 重複する時刻の操作について0,1,bool型で指定する。
 :type fold: int|bool
 :raises TypeError: `year`でint型ではない型を指定した場合に発生させる。
 :raises ValueError: `times.maxsyear<=year<=times.minsyear`を超えた値を指定した場合に発生させる。
 :raises TypeError: `month`でint型ではない型を指定した場合に発生させる。
 :raises ValueError: `1<=month<=12`を超えた値を指定した場合に発生させる。
 :raises TypeError: `day`でint型ではない型を指定した場合に発生させる。
 :raises ValueError: `1<=day<=指定された年と月の日数`を超えた値を指定した場合に発生させる。
 :raises TypeError: `hour`でint型ではない型を指定した場合に発生させる。
 :raises ValueError: `0<=hour<=24`を超えた値を指定した場合に発生させる。
 :raises TypeError: `minute`でint型ではない型を指定した場合に発生させる。
 :raises ValueError: `0<=minute<=60`を超えた値を指定した場合に発生させる。
 :raises TypeError: `second`でint型ではない型を指定した場合に発生させる。
 :raises ValueError: `0<=second<=60`を超えた値を指定した場合に発生させる。
 :raises TypeError: `microsecond`でint型ではない型を指定した場合に発生させる。
 :raises ValueError: `0<=microsecond<=1000000`を超えた値を指定した場合に発生させる。'''
 @overload
 def __init__(
self,
dates:datetime.datetime|datetime.date|times|None=None
)->None:'''日付と時間を作成するクラス'''
 def __eq__(self,val:datetime.datetime|datetime.date|times)->bool:''':return: `self`==`val`を返す。
 :rtype: bool'''
 def __ne__(self,val:datetime.datetime|datetime.date|times)->bool:''':return: `self`!=`val`を返す。
 :rtype: bool'''
 def __lt__(self,val:datetime.datetime|datetime.date|times)->bool:''':return: `self`<`val`を返す。
 :rtype: bool'''
 def __le__(self,val:datetime.datetime|datetime.date|times)->bool:''':return: `self`<=`val`を返す。
 :rtype: bool'''
 def __gt__(self,val:datetime.datetime|datetime.date|times)->bool:''':return: `self`>`val`を返す。
 :rtype: bool'''
 def __ge__(self,val:datetime.datetime|datetime.date|times)->bool:''':return: `self`>=`val`を返す。
 :rtype: bool'''
 def __add__(self,val:datetime.timedelta)->times:''':return: `self`+`val`を返す。
 :rtype: times'''
 def __sub__(self,val:datetime.timedelta)->times:''':return: `self`-`val`を返す。
 :rtype: times'''
 def __radd__(self,val:datetime.timedelta)->times:''':return: `self`+`val`を返す。
 :rtype: times'''
 def __rsub__(self,val:datetime.timedelta)->times:''':return: `self`-`val`を返す。
 :rtype: times'''
 def date(self)->datetime.datetime|None:'''日付時刻を返す。

 :return: 日付時刻を返す。
 :rtype: datetime.datetime|None'''
 def getdate(self)->tuple[int,int,int,int,int,int,int]:'''日付時刻の値を返す。'''
 def astimezone(self,timezone:datetime._TzInfo='Asia/Tokyo')->datetime.datetime:...
 def time(self)->datetime._Time:...
 def timetz(self)->datetime._Time:...
 def utcoffset(self)->datetime.timedelta|None:...
 def dst(self)->datetime.timedelta|None:...
 def tzname(self)->str|None:...
 def timetuple(self)->time.struct_time:...
 def utctimetuple(self)->time.struct_time:...
 def toordinal(self)->int:...
 def timestamp(self)->float:...
 def weekday(self)->int:...
 def isoweekday(self)->int:...
 def isocalendar(self)->datetime._IsoCalendarDate:...
 def ctime(self)->str:...
 def strptime(self,format:str='%Y/%m/%d,%H:%M:%S')->datetime.datetime:...
 def strftime(self,format:str='%Y/%m/%d,%H:%M:%S')->str:...
 def replace(
self,
year:int=...,
month:int=...,
day:int=...,
hour:int=...,
minute:int=...,
second:int=...,
microsecond:int=...,
timezone:datetime._TzInfo=...,
fold:int=...
)->times:...
 def __str__(self)->str:...
 @overload
 def min(self)->datetime.datetime:'''表現できる最も古い日付のdatetime.datetime(`minsyear`,1,1)を返す。

 :return: 表現できる最も古い日付のdatetime.datetime(`minsyear`,1,1)を返す。
 :rtype: datetime.datetime'''
 @overload
 @staticmethod
 def min()->datetime.datetime:'''表現できる最も古い日付のdatetime.datetime(`minsyear`,1,1)を返す。

 :return: 表現できる最も古い日付のdatetime.datetime(`minsyear`,1,1)を返す。
 :rtype: datetime.datetime'''
 def max(self)->datetime.datetime:'''表現できる最も新しい日付のdatetime.datetime(`maxsyear`,12,31)を返す。

 :return: 表現できる最も新しい日付のdatetime.datetime(`maxsyear`,12,31)を返す。
 :rtype: datetime.datetime'''
 @staticmethod
 def max()->datetime.datetime:'''表現できる最も新しい日付のdatetime.datetime(`maxsyear`,12,31)を返す。

 :return: 表現できる最も新しい日付のdatetime.datetime(`maxsyear`,12,31)を返す。
 :rtype: datetime.datetime'''
 @staticmethod
 def now(timezone:datetime._TzInfo='Asia/Tokyo')->times:'''現在のローカル日付日時を返す。

 :param timezone: タイムゾーンを指定する。
 :type timezone: datetime._TzInfo
 :return: 現在のローカル日付日時を返す。
 :rtype: times'''
 @staticmethod
 def today(timezone:datetime._TzInfo='Asia/Tokyo')->times:'''現在のローカル日付を返す。

 :param timezone: タイムゾーンを指定する。
 :type timezone: datetime._TzInfo
 :return: 現在のローカル日付を返す。
 :rtype: times'''
 @staticmethod
 def maxyear(maxs:int)->NoReturn:'''`year`の範囲の最大の年を変更する。

 :param maxs: 最大の年を指定する。1<=`maxs`<=9999の範囲を超えた値を指定した場合9999にする。
 :type maxs: int'''
 def minyear(mins:int)->NoReturn:'''`year`の範囲の最小の年を変更する。

 :param mins: 最小の年を指定する。1<=`mins`<=9999の範囲を超えた値を指定した場合1にする。
 :type mins: int'''
class timeslist:
 datelist:tuple[datetime.datetime|None]
 def __init__(
self,
dates:str|datetime.datetime|datetime.date|times|Listlike[str|datetime.datetime|datetime.date|times,...]
)->None:...
 @classmethod
 def __instancecheck__(cls,ins:Any)->bool:...
 def __len__(self)->int:...
 def __iter__(self)->Iterator[datetime.datetime]:...
 @overload
 def __getitem__(self,val:int|slice)->Any|list:...
 @overload
 def __getitem__(self,val:int)->Any:...
 @overload
 def __getitem__(self,val:slice)->list:...