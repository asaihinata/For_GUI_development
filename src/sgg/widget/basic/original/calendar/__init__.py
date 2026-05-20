from datetime import date,datetime
from ...common import *
from ._calendar import Calendar
logger=Logger(format={'filename':None,'lineno':{'after':'行目'},'message':None}).get_logger()
__all__=['Calendars']
fotmat_list={'format0':'yyyy/mm/dd','format1':'yyyy-mm-dd','format2':'dd/mm/yyyy','format3':'dd-mm-yyyy'}
class Calendars(Element):
 def _format(self,val):return fotmat_list.get(val,'yyyy/mm/dd')
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.borderwidth=num0(kw.get('bd'))
  self.dates=kw.get('date') if isinstance(kw.get('date'),datetime|date) else date.today()
  self.year,self.month,self.day=self.dates.year,self.dates.month,self.dates.day
  self.showweek=bols(kw.get('showweek'),False)
  self.showotherdays=bols(kw.get('showotherdays'))
  self.selectmode=listchose(kw.get('selectmode'),['day','none'])
  self.format=self._format(kw.get('format'))
  self.headersbackground=parsecolor(kw.get('headersbg'),'gray70')
  self.headersforeground=parsecolor(kw.get('headersfg'),'black')
  self.othermonthbackground=parsecolor(kw.get('othermonthbg'),'gray93')
  self.othermonthforeground=parsecolor(kw.get('othermonthfg'),'gray45')
  self.weekendbackground=parsecolor(kw.get('weekendbg'),'gray80')
  self.weekendforeground=parsecolor(kw.get('weekendfg'),'gray30')
  self.weekenddays=kw.get('weekenddays')
  self.locale=kw.get('locale','ja_JP')
  self.textvariable=kw.get('textvariable')
  self.firstweekday=kw.get('firstweekday','sunday')
  self.maxdate=kw.get('maxdate')
  if not isinstance(self.maxdate,datetime):self.maxdate=None
  self.mindate=kw.get('mindate')
  if not isinstance(self.mindate,datetime):self.mindate=None
  self.widget=Calendar(master,textvariable=self.textvariable,showothermonthdays=self.showotherdays,maxdate=self.maxdate,mindate=self.mindate,weekenddays=self.weekenddays,firstweekday=self.firstweekday,locale=self.locale,weekendforeground=self.weekendforeground,weekendbackground=self.weekendbackground,othermonthforeground=self.othermonthforeground,othermonthbackground=self.othermonthbackground,headersbackground=self.headersbackground,headersforeground=self.headersforeground,selectmode=self.selectmode,year=self.year,month=self.month,day=self.day,font=self.font,showweeknumbers=self.showweek,date_pattern=self.format)
 def move_date(self,year=None,month=None,day=None):
  now=date(year,month,day)
  self.widget.selection_set(now)
  self.widget.configure(year=year,month=month)
 def move_today(self):
  now=datetime.today()
  self.move_date(year=now.year,month=now.month,day=now.day)
 def move_select(self):
  selects=self.get_select()
  self.widget.selection_set(selects)
  self.widget.configure(year=selects.year,month=selects.month)
 def get_select(self):return self.widget.selection_get()
 def get_date(self):return self.widget.get_date()
 def select_clear(self):return self.widget.selection_clear()
 def nowdate_show(self):return self.widget.get_displayed_month()
 def delta(self):
  try:self.widget.destroy()
  except Exception as e:
   logger.error(e)