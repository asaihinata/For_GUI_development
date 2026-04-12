'''日付や時間に関するモジュール'''
from calendar import monthrange
import datetime
from zoneinfo import ZoneInfo,available_timezones
__all__=['times']
class times:
 maxsyear,minsyear,datetimes=9999,1,None
 @classmethod
 def __instancecheck__(cls,ins):return isinstance(ins,times)
 def __init__(self,year=None,month=None,day=None,hour=0,minute=0,second=0,microsecond=0,timezone='Asia/Tokyo',fold=0,date=None):
  if isinstance(date,(datetime.datetime,datetime.date)):self.datetimes=date
  elif isinstance(date,times):self.datetimes=date.datetimes
  else:
   self.year=self._valset(year,'year',self.minsyear,self.maxsyear)
   self.month=self._valset(month,'month',1,12)
   self.day=self._valset(day,'day',1,monthrange(self.year,self.month)[1])
   self.hour=self._valset(hour,'hour',0,24)
   self.minute=self._valset(minute,'minute',0,60)
   self.second=self._valset(second,'second',0,60)
   self.microsecond=self._valset(microsecond,'microsecond',0,1000000)
   self.timezone=_timezonecheck(timezone)
   self.fold=_fold(fold)
   self.datetimes=datetime.datetime(self.year,self.month,self.day,self.hour,self.minute,self.second,self.microsecond,tzinfo=self.timezone,fold=self.fold)
 def _valset(self,val,name,mins,maxs):
  if not isinstance(val,int):
   raise TypeError(f'{name}にint型を指定してください')
  elif not mins<=val<=maxs:
   raise ValueError(f'{name}には{mins}<={name}<={maxs}の範囲内で指定してください')
  else:return val
 def date(self):return self.datetimes
 def astimezone(self,timezone='Asia/Tokyo'):return self.datetimes.astimezone(_timezonecheck(timezone))
 def time(self):return self.datetimes.time()
 def timetz(self):return self.datetimes.timetz()
 def utcoffset(self):return self.datetimes.utcoffset()
 def dst(self):return self.datetimes.dst()
 def tzname(self):return self.datetimes.tzname()
 def timetuple(self):return self.datetimes.timetuple()
 def utctimetuple(self):return self.datetimes.utctimetuple()
 def toordinal(self):return self.datetimes.toordinal()
 def timestamp(self):return self.datetimes.timestamp()
 def weekday(self):return self.datetimes.weekday()
 def isoweekday(self):return self.datetimes.isoweekday()
 def isocalendar(self):return self.datetimes.isocalendar()
 def ctime(self):return self.datetimes.ctime()
 def strftime(self,format='%Y/%m/%d,%H:%M:%S'):return self.datetimes.strftime(format)
 def replace(self,year=None,month=None,day=None,hour=None,minute=None,second=None,microsecond=None,timezone=True,fold=None):
  if year is None:year=self.year
  if month is None:month=self.month
  if day is None:day=self.day
  if hour is None:hour=self.hour
  if minute is None:minute=self.minute
  if second is None:second=self.second
  if microsecond is None:microsecond=self.microsecond
  if timezone is True:tzinfo=self.timezone
  if fold is None:fold=self.fold
  return times(year,month,day,hour,minute,second,microsecond,tzinfo,fold=fold)
 def __str__(self):return str(self.datetimes)
 def min(self):return datetime.datetime(self.minsyear,1,1)
 def max(self):return datetime.datetime(self.maxsyear,12,31)
 @staticmethod
 def min():return datetime.datetime(times.minsyear,1,1)
 @staticmethod
 def max():return datetime.datetime(times.maxsyear,12,31)
 @staticmethod
 def now(timezone='Asia/Tokyo'):return times(date=datetime.datetime.now(_timezonecheck(timezone)))
 @staticmethod
 def today(timezone='Asia/Tokyo'):return times(date=datetime.datetime.now(_timezonecheck(timezone)).date())
 @staticmethod
 def maxyear(maxs):
  if isinstance(maxs,int):
   maxs,mins=maxs,times.minsyear
   if maxs<mins:mins,maxs=maxs,mins
   if not 1<=maxs<=9999:maxs=9999
   if not 1<=mins<=9999:mins=1
   times.minsyear,times.maxsyear=mins,maxs
 @staticmethod
 def minyear(mins):
  if isinstance(mins,int):
   maxs,mins=times.maxsyear,mins
   if maxs<mins:mins,maxs=maxs,mins
   if not 1<=maxs<=9999:maxs=9999
   if not 1<=mins<=9999:mins=1
   times.minsyear,times.maxsyear=mins,maxs
def _timezonecheck(time):return ZoneInfo(time if time in available_timezones() else 'Asia/Tokyo')
def _fold(val):return int(val) if isinstance(val,bool)or(val in [0,1]) else 0