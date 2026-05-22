from datetime import datetime
from ....base import _Element
from .....typing import TupleInt2
class Calendars(_Element):
 def delta(self):'''ウィジェットを削除する。'''
 def move_date(self,year:int=None,month:int=None,day:int=None):'''指定したyear,month,dayに移動する。

 :param year: 移動先の年を指定する。
 :type year: int
 :param month: 移動先の月を指定する。
 :type month: int
 :param day: 移動先の日にちを指定する。
 :type day: int'''
 def move_today(self):'''本日の日付に移動する。'''
 def move_select(self):'''Calendarsウィジェットで指定されている日付に移動する。'''
 def get_select(self)->datetime:'''Calendarsウィジェットで指定されている日付を取得する。'''
 def get_date(self)->str:'''Calendarsウィジェットで選択されている日にちを文字列で返す。

 :return: Calendarsウィジェットで選択されている日にちを文字列で返す。
 :rtype: str'''
 def select_clear(self):'''Calendarsウィジェットに選択されている日付を消す。'''
 def nowdate_show(self)->TupleInt2:'''Calendarsウィジェットで表示されている年と月をタプルで(月,年)で返す。

 :return: Calendarsウィジェットで表示されている年と月をタプルで(月,年)で返す。
 :rtype: TupleInt2'''