from calendar import TextCalendar,monthrange
from datetime import datetime,timedelta
from re import findall,search
from tkinter import StringVar
from tkinter.ttk import Button,Frame,Label,Style
from babel.core import default_locale
from babel.dates import format_date,get_date_format,get_day_names,get_month_names,parse_date
from ..._function import listchose,num0
from .tooltip import TooltipWrapper
class Calendar(Frame):
 date=datetime.date
 def __init__(self,master,**kw):
  self.font=kw.get('font')
  curs=kw.get('cursor')
  classname=kw.get('class_','Calendar')
  name=kw.get('name')
  Frame.__init__(self,master,class_=classname,cursor=curs,name=name)
  self._style_prefixe=str(self)
  Frame.configure(self,style='main.%s.TFrame'%self._style_prefixe)
  self._textvariable=kw.get('textvariable')
  if not isinstance(self._textvariable,StringVar):self._textvariable=None
  prop=self.font.actual()
  prop['size']+=1
  self._header_font=self.font
  state=listchose(kw.get('state'),['normal','disabled'])
  bd=num0(kw.get('borderwidth',2))
  self.firstweekday=kw.get('firstweekday','sunday')
  if self.firstweekday not in ['monday','sunday']:
   raise ValueError('\'firstweekday\'オプションは\'monday\'または\'sunday\'にする必要があります')
  self._cal=TextCalendar((self.firstweekday=='sunday')*6)
  self.weekenddays=kw.get('weekenddays')
  if not self.weekenddays:
   l=list(self._cal.iterweekdays())
   self.weekenddays=[l.index(5)+1,l.index(6)+1]
  self._check_weekenddays(self.weekenddays)
  locale=kw.get('locale',default_locale())
  if locale==None:locale='ja'
  self._day_names=get_day_names('abbreviated',locale=locale)
  self._month_names=get_month_names('wide',locale=locale)
  date_pattern=self._get_date_pattern(kw.get('date_pattern','short'),locale)
  today=datetime.today()
  if self._textvariable!=None:
   try:
    self._sel_date=parse_date(self._textvariable.get(),locale)
    month,year=self._sel_date.month,self._sel_date.year
   except IndexError:
    self._sel_date=None
    self._textvariable.set('')
    month,year=kw.get('month',today.month),kw.get('year',today.year)
  else:
   if (('month' in kw) or ('year' in kw))and('day' not in kw):
    month,year=kw.get('month',today.month),kw.get('year',today.year)
    self._sel_date=None
   else:
    day=kw.get('day',today.day)
    month=kw.get('month',today.month)
    year=kw.get('year',today.year)
    try:self._sel_date=datetime(year,month,day)
    except ValueError:self._sel_date=None
  self._date=datetime(year,month,1)
  maxdate=kw.get('maxdate')
  mindate=kw.get('mindate')
  if maxdate!=None:
   if isinstance(maxdate,datetime):maxdate=maxdate.date()
   else:
    raise TypeError('expected %s for the \'maxdate\' option.'%datetime)
  if mindate!=None:
   if isinstance(mindate,datetime):mindate=mindate.date()
   else:
     raise TypeError('expected %s for the \'mindate\' option.'%datetime)
  if mindate!=None and maxdate!=None and maxdate<mindate:mindate,maxdate=maxdate,mindate
  selectmode=listchose(kw.get('selectmode'),['day','none'])
  showweeknumbers=kw.get('showweeknumbers',True)
  self.style=Style(self)
  active_bg=self.style.lookup('TEntry','selectbackground',('focus',))
  dis_active_bg=self.style.lookup('TEntry','selectbackground',('disabled',))
  dis_bg=self.style.lookup('TLabel','background',('disabled',))
  dis_fg=self.style.lookup('TLabel','foreground',('disabled',))
  keys=list(kw.keys())
  for option in keys:
   if option not in ['cursor','font','borderwidth','state','selectmode','textvariable','locale','date_pattern','maxdate','mindate','showweeknumbers','showothermonthdays','firstweekday','weekenddays','selectbackground','selectforeground','disabledselectbackground','disabledselectforeground','normalbackground','normalforeground','background','foreground','disabledbackground','disabledforeground','bordercolor','othermonthforeground','othermonthbackground','othermonthweforeground','othermonthwebackground','weekendbackground','weekendforeground','headersbackground','headersforeground','disableddaybackground','disableddayforeground','tooltipforeground','tooltipbackground','tooltipalpha','tooltipdelay']:del(kw[option])
  self._properties={'cursor':curs,'font':self.font,'borderwidth':bd,'state':state,'locale':locale,'date_pattern':date_pattern,'selectmode':selectmode,'textvariable':self._textvariable,'firstweekday':self.firstweekday,'weekenddays':self.weekenddays,'mindate':mindate,'maxdate':maxdate,'showweeknumbers':showweeknumbers,'showothermonthdays':kw.get('showothermonthdays',True),'selectbackground':active_bg,'selectforeground':'white','disabledselectbackground':dis_active_bg,'disabledselectforeground':'white','normalbackground':'white','normalforeground':'black','background':'gray30','foreground':'white','disabledbackground':'gray30','disabledforeground':'gray70','bordercolor':'gray70','othermonthforeground':'gray45','othermonthbackground':'gray93','othermonthweforeground':'gray45','othermonthwebackground':'gray75','weekendbackground':'gray80','weekendforeground':'gray30','headersbackground':'gray70','headersforeground':'black','disableddaybackground':dis_bg,'disableddayforeground':dis_fg,'tooltipforeground':'gray90','tooltipbackground':'black','tooltipalpha':0.8,'tooltipdelay':2000}
  self._properties.update(kw)
  self.calevents={}
  self._calevent_dates={}
  self._tags={}
  self.tooltip_wrapper=TooltipWrapper(self,alpha=self._properties['tooltipalpha'],style=self._style_prefixe+'.tooltip.TLabel',delay=self._properties['tooltipdelay'])
  self._header=Frame(self,style='main.%s.TFrame'%self._style_prefixe)
  f_month=Frame(self._header,style='main.%s.TFrame'%self._style_prefixe)
  self._l_month=Button(f_month,style='L.%s.TButton'%self._style_prefixe,command=self._prev_month)
  self._header_month=Label(f_month,width=10,anchor='center',style='main.%s.TLabel'%self._style_prefixe,font=self._header_font)
  self._r_month=Button(f_month,style='R.%s.TButton'%self._style_prefixe,command=self._next_month)
  self._l_month.pack(side='left',fill='y')
  self._header_month.pack(side='left',padx=4)
  self._r_month.pack(side='left',fill='y')
  f_year=Frame(self._header,style='main.%s.TFrame'%self._style_prefixe)
  self._l_year=Button(f_year,style='L.%s.TButton'%self._style_prefixe,command=self._prev_year)
  self._header_year=Label(f_year,width=4,anchor='center',style='main.%s.TLabel'%self._style_prefixe,font=self._header_font)
  self._r_year=Button(f_year,style='R.%s.TButton'%self._style_prefixe,command=self._next_year)
  self._l_year.pack(side='left',fill='y')
  self._header_year.pack(side='left',padx=4)
  self._r_year.pack(side='left',fill='y')
  f_month.pack(side='left',fill='x')
  f_year.pack(side='right')
  self._cal_frame=Frame(self,style='cal.%s.TFrame'%self._style_prefixe)
  Label(self._cal_frame,style='headers.%s.TLabel'%self._style_prefixe).grid(row=0,column=0,sticky='eswn')
  self._week_days=[]
  for i,day in enumerate(self._cal.iterweekdays()):
   d=self._day_names[day%7]
   self._cal_frame.columnconfigure(i+1,weight=1)
   self._week_days.append(Label(self._cal_frame,font=self.font,style='headers.%s.TLabel'%self._style_prefixe,anchor='center',text=d,width=4))
   self._week_days[-1].grid(row=0,column=i+1,sticky='ew',pady=(0,1))
  self._week_nbs,self._calendar=[],[]
  for i in range(1,7):
   self._cal_frame.rowconfigure(i,weight=1)
   wlabel=Label(self._cal_frame,style='headers.%s.TLabel'%self._style_prefixe,font=self.font,padding=2,anchor='e',width=1)
   self._week_nbs.append(wlabel)
   wlabel.grid(row=i,column=0,sticky='esnw',padx=(0,1))
   if not showweeknumbers:wlabel.grid_remove()
   self._calendar.append([])
   for j in range(1,8):
    label=Label(self._cal_frame,style='normal.%s.TLabel'%self._style_prefixe,font=self.font,anchor='center')
    self._calendar[-1].append(label)
    label.grid(row=i,column=j,padx=(0,1),pady=(0,1),sticky='nsew')
    if selectmode=='day':label.bind('<1>',self._on_click)
  self._header.pack(fill='x',padx=2,pady=2)
  self._cal_frame.pack(fill='both',expand=True,padx=bd,pady=bd)
  self.config(state=state)
  self.bind('<<ThemeChanged>>',self._setup_style)
  self._setup_style()
  self._display_calendar()
  self._btns_date_range()
  self._check_sel_date()
  if self._textvariable!=None:
   try:self._textvariable_trace_id=self._textvariable.trace_add('write',self._textvariable_trace)
   except AttributeError:self._textvariable_trace_id=self._textvariable.trace('w',self._textvariable_trace)
 def __getitem__(self,key):
  try:return self._properties[key]
  except KeyError:
   raise AttributeError('Calendar object has no attribute %s.'%key)
 def __setitem__(self,key,value):
  if key not in self._properties:
   raise AttributeError('Calendar object has no attribute %s.'%key)
  elif key=='date_pattern':
   date_pattern=self._get_date_pattern(value)
   self._properties[key]=date_pattern
  else:
   if key=='selectmode':
    if value=='none':
     for week in self._calendar:
      for day in week:day.unbind('<1>')
    elif value=='day':
     for week in self._calendar:
      for day in week:day.bind('<1>',self._on_click)
    else:
     raise ValueError('\'selectmode\' option should be \'none\' or \'day\'.')
   elif key=='locale':
    self._day_names=get_day_names('abbreviated',locale=value)
    self._month_names=get_month_names('wide',locale=value)
    self._properties['date_pattern']=self._get_date_pattern('short',value)
    for i,l in enumerate(self._week_days):l.configure(text=self._day_names[i])
    self._header_month.configure(text=self._month_names[self._date.month].title())
   elif key=='textvariable':
    try:
     if self._textvariable!=None:self._textvariable.trace_remove('write',self._textvariable_trace_id)
     if value!=None:self._textvariable_trace_id=value.trace_add('write',self._textvariable_trace)
    except AttributeError:
     if self._textvariable!=None:self._textvariable.trace_vdelete('w',self._textvariable_trace_id)
     if value!=None:value.trace('w',self._textvariable_trace)
    self._textvariable=value
    value.set(value.get())
   elif key=='showweeknumbers':
    if value:
     for wlabel in self._week_nbs:wlabel.grid()
    else:
     for wlabel in self._week_nbs:wlabel.grid_remove()
   elif key=='firstweekday':
    if value not in ['monday','sunday']:
     raise ValueError('\'firstweekday\' option should be \'monday\' or \'sunday\'.')
    self._cal.firstweekday=(value=='sunday')*6
    for label,day in zip(self._week_days,self._cal.iterweekdays()):label.configure(text=self._day_names[day%7])
   elif key=='weekenddays':self._check_weekenddays(value)
   elif key=='borderwidth':
    try:
     bd=int(value)
     self._cal_frame.pack_configure(padx=bd,pady=bd)
    except ValueError:
     raise ValueError('expected integer for the borderwidth option.')
   elif key=='state':
    if value not in ['normal','disabled']:value='normal'
    state='!'*(value=='normal')+'disabled'
    self.state((state,))
    self._header.state((state,))
    for child in self._header.children.values():child.state((state,))
    self._header_month.state((state,))
    self._header_year.state((state,))
    self._l_year.state((state,))
    self._r_year.state((state,))
    self._l_month.state((state,))
    self._r_month.state((state,))
    for child in self._cal_frame.children.values():child.state((state,))
   elif key=='maxdate':
    if value!=None:
     if isinstance(value,datetime):value=value.date()
     elif not isinstance(value,datetime):
      raise TypeError('expected %s for the \'maxdate\' option.'%datetime)
     mindate=self['mindate']
     if mindate!=None and mindate>value:
      self._properties['mindate']=value
      self._date=self._date.replace(year=value.year,month=value.month)
     elif self._date>value:self._date=self._date.replace(year=value.year,month=value.month)
    self._r_month.state(['!disabled'])
    self._r_year.state(['!disabled'])
    self._l_month.state(['!disabled'])
    self._l_year.state(['!disabled'])
   elif key=='mindate':
    if value!=None:
     if isinstance(value,datetime):value=value.date()
     elif not isinstance(value,datetime):
      raise TypeError('expected %s for the \'mindate\' option.'%datetime)
     maxdate=self['maxdate']
     if maxdate!=None and maxdate<value:
      self._properties['maxdate']=value
      self._date=self._date.replace(year=value.year,month=value.month)
     elif self._date<value:self._date=self._date.replace(year=value.year,month=value.month)
    self._r_month.state(['!disabled'])
    self._r_year.state(['!disabled'])
    self._l_month.state(['!disabled'])
    self._l_year.state(['!disabled'])
   elif key=='font':
    prop=self.font.actual()
    self.font.configure(**prop)
    prop['size']+=1
    self._header_font.configure(**prop)
    size=max(prop['size'],10)
    self.style.configure('R.%s.TButton'%self._style_prefixe,arrowsize=size)
    self.style.configure('L.%s.TButton'%self._style_prefixe,arrowsize=size)
   elif key=='normalbackground':
    self.style.configure('cal.%s.TFrame'%self._style_prefixe,background=value)
    self.style.configure('normal.%s.TLabel'%self._style_prefixe,background=value)
    self.style.configure('normal_om.%s.TLabel'%self._style_prefixe,background=value)
   elif key=='normalforeground':self.style.configure('normal.%s.TLabel'%self._style_prefixe,foreground=value)
   elif key=='bordercolor':self.style.configure('cal.%s.TFrame'%self._style_prefixe,background=value)
   elif key=='othermonthforeground':self.style.configure('normal_om.%s.TLabel'%self._style_prefixe,foreground=value)
   elif key=='othermonthbackground':self.style.configure('normal_om.%s.TLabel'%self._style_prefixe,background=value)
   elif key=='othermonthweforeground':self.style.configure('we_om.%s.TLabel'%self._style_prefixe,foreground=value)
   elif key=='othermonthwebackground':self.style.configure('we_om.%s.TLabel'%self._style_prefixe,background=value)
   elif key=='selectbackground':self.style.configure('sel.%s.TLabel'%self._style_prefixe,background=value)
   elif key=='selectforeground':self.style.configure('sel.%s.TLabel'%self._style_prefixe,foreground=value)
   elif key=='disabledselectbackground':self.style.map('sel.%s.TLabel'%self._style_prefixe,background=[('disabled',value)])
   elif key=='disabledselectforeground':self.style.map('sel.%s.TLabel'%self._style_prefixe,foreground=[('disabled',value)])
   elif key=='disableddaybackground':self.style.map('%s.TLabel'%self._style_prefixe,background=[('disabled',value)])
   elif key=='disableddayforeground':self.style.map('%s.TLabel'%self._style_prefixe,foreground=[('disabled',value)])
   elif key=='weekendbackground':
    self.style.configure('we.%s.TLabel'%self._style_prefixe,background=value)
    self.style.configure('we_om.%s.TLabel'%self._style_prefixe,background=value)
   elif key=='weekendforeground':self.style.configure('we.%s.TLabel'%self._style_prefixe,foreground=value)
   elif key=='headersbackground':self.style.configure('headers.%s.TLabel'%self._style_prefixe,background=value)
   elif key=='headersforeground':self.style.configure('headers.%s.TLabel'%self._style_prefixe,foreground=value)
   elif key=='background':
    self.style.configure('main.%s.TFrame'%self._style_prefixe,background=value)
    self.style.configure('main.%s.TLabel'%self._style_prefixe,background=value)
    self.style.configure('R.%s.TButton'%self._style_prefixe,background=value,bordercolor=value,lightcolor=value,darkcolor=value)
    self.style.configure('L.%s.TButton'%self._style_prefixe,background=value,bordercolor=value,lightcolor=value,darkcolor=value)
   elif key=='foreground':
    self.style.configure('R.%s.TButton'%self._style_prefixe,arrowcolor=value)
    self.style.configure('L.%s.TButton'%self._style_prefixe,arrowcolor=value)
    self.style.configure('main.%s.TLabel'%self._style_prefixe,foreground=value)
   elif key=='disabledbackground':
    self.style.map('%s.TButton'%self._style_prefixe,background=[('active','!disabled',self.style.lookup('TEntry','selectbackground',('focus',))),('disabled',value)],)
    self.style.map('main.%s.TFrame'%self._style_prefixe,background=[('disabled',value)])
    self.style.map('main.%s.TLabel'%self._style_prefixe,background=[('disabled',value)])
   elif key=='disabledforeground':
    self.style.map('%s.TButton'%self._style_prefixe,arrowcolor=[('disabled',value)])
    self.style.map('main.%s.TLabel'%self._style_prefixe,foreground=[('disabled',value)])
   elif key=='cursor':Frame.configure(self,cursor=value)
   elif key=='tooltipbackground':self.style.configure('%s.tooltip.TLabel'%self._style_prefixe,background=value)
   elif key=='tooltipforeground':self.style.configure('%s.tooltip.TLabel'%self._style_prefixe,foreground=value)
   elif key=='tooltipalpha':self.tooltip_wrapper.configure(alpha=value)
   elif key=='tooltipdelay':self.tooltip_wrapper.configure(delay=value)
   self._properties[key]=value
   if key in ['showothermonthdays','firstweekday','weekenddays','maxdate','mindate']:
    self._display_calendar()
    self._check_sel_date()
    self._btns_date_range()
 def _check_weekenddays(self,days):
  set_day=days
  if isinstance(days,(list,tuple)):
   if len(days)==2:
    if set_day[0] not in range(1,8):set_day[0]=1
    if set_day[1] not in range(1,8):set_day[1]=7
    if set_day[0]==set_day[1]:set_day=[1,7]
   else:set_day=[1,7]
  else:set_day=[1,7]
  self.weekenddays=set_day
 def _textvariable_trace(self,*args):
  if self._properties.get('selectmode')=='day':
   date=self._textvariable.get()
   if not date:
    self._remove_selection()
    self._sel_date=None
   else:
    try:self._sel_date=self.parse_date(date)
    except Exception:
     if self._sel_date==None:self._textvariable.set('')
     else:self._textvariable.set(self.format_date(self._sel_date))
     raise ValueError(f'{date}は有効な日付パターンではありません')
    else:
     self._date=self._sel_date.replace(day=1)
     self._display_calendar()
     self._display_selection()
 def _setup_style(self,event=None):
  self.style.layout('L.%s.TButton'%self._style_prefixe,[('Button.focus',{'children':[('Button.leftarrow',None)]})])
  self.style.layout('R.%s.TButton'%self._style_prefixe,[('Button.focus',{'children':[('Button.rightarrow',None)]})])
  active_bg=self.style.lookup('TEntry','selectbackground',('focus',))
  sel_bg=self._properties.get('selectbackground')
  sel_fg=self._properties.get('selectforeground')
  dis_sel_bg=self._properties.get('disabledselectbackground')
  dis_sel_fg=self._properties.get('disabledselectforeground')
  dis_day_bg=self._properties.get('disableddaybackground')
  dis_day_fg=self._properties.get('disableddayforeground')
  cal_bg=self._properties.get('normalbackground')
  cal_fg=self._properties.get('normalforeground')
  hd_bg=self._properties.get('headersbackground')
  hd_fg=self._properties.get('headersforeground')
  bg=self._properties.get('background')
  fg=self._properties.get('foreground')
  dis_bg=self._properties.get('disabledbackground')
  dis_fg=self._properties.get('disabledforeground')
  bc=self._properties.get('bordercolor')
  om_fg=self._properties.get('othermonthforeground')
  om_bg=self._properties.get('othermonthbackground')
  omwe_fg=self._properties.get('othermonthweforeground')
  omwe_bg=self._properties.get('othermonthwebackground')
  we_bg=self._properties.get('weekendbackground')
  we_fg=self._properties.get('weekendforeground')
  self.style.configure('main.%s.TFrame'%self._style_prefixe,background=bg)
  self.style.configure('cal.%s.TFrame'%self._style_prefixe,background=bc)
  self.style.configure('main.%s.TLabel'%self._style_prefixe,background=bg,foreground=fg)
  self.style.configure('headers.%s.TLabel'%self._style_prefixe,background=hd_bg,foreground=hd_fg)
  self.style.configure('normal.%s.TLabel'%self._style_prefixe,background=cal_bg,foreground=cal_fg)
  self.style.configure('normal_om.%s.TLabel'%self._style_prefixe,background=om_bg,foreground=om_fg)
  self.style.configure('we_om.%s.TLabel'%self._style_prefixe,background=omwe_bg,foreground=omwe_fg)
  self.style.configure('sel.%s.TLabel'%self._style_prefixe,background=sel_bg,foreground=sel_fg)
  self.style.configure('we.%s.TLabel'%self._style_prefixe,background=we_bg,foreground=we_fg)
  size=max(self._header_font.actual()['size'],10)
  self.style.configure('%s.TButton'%self._style_prefixe,background=bg,arrowcolor=fg,arrowsize=size,bordercolor=bg,relief='flat',lightcolor=bg,darkcolor=bg)
  self.style.configure('%s.tooltip.TLabel'%self._style_prefixe,background=self._properties['tooltipbackground'],foreground=self._properties['tooltipforeground'])
  self.style.map('%s.TButton'%self._style_prefixe,background=[('active','!disabled',active_bg),('disabled',dis_bg)],bordercolor=[('active',active_bg)],relief=[('active','flat')],arrowcolor=[('disabled',dis_fg)],darkcolor=[('active',active_bg)],lightcolor=[('active',active_bg)])
  self.style.map('main.%s.TFrame'%self._style_prefixe,background=[('disabled',dis_bg)])
  self.style.map('main.%s.TLabel'%self._style_prefixe,background=[('disabled',dis_bg)],foreground=[('disabled',dis_fg)])
  self.style.map('sel.%s.TLabel'%self._style_prefixe,background=[('disabled',dis_sel_bg)],foreground=[('disabled',dis_sel_fg)])
  self.style.map(self._style_prefixe+'.TLabel',background=[('disabled',dis_day_bg)],foreground=[('disabled',dis_day_fg)])
 def _display_calendar(self):
  year=self._date.year
  month=self._date.month
  self._header_month.configure(text=self._month_names[month].title())
  self._header_year.configure(text=str(year))
  self.tooltip_wrapper.remove_all()
  if self['showothermonthdays']:self._display_days_with_othermonthdays()
  else:self._display_days_without_othermonthdays()
  self._display_selection()
  maxdate,mindate=self['maxdate'],self['mindate']
  if maxdate!=None:
   mi,mj=self._get_day_coords(maxdate)
   if mi!=None:
    for j in range(mj+1,7):self._calendar[mi][j].state(['disabled'])
    for i in range(mi+1,6):
     for j in range(7):self._calendar[i][j].state(['disabled'])
  if mindate!=None:
   mi,mj=self._get_day_coords(mindate)
   if mi!=None:
    for j in range(mj):self._calendar[mi][j].state(['disabled'])
    for i in range(mi):
     for j in range(7):self._calendar[i][j].state(['disabled'])
 def _display_days_without_othermonthdays(self):
  year,month=self._date.year,self._date.month
  cal=self._cal.monthdays2calendar(year,month)
  while len(cal)<6:cal.append([(0,i) for i in range(7)])
  week_days={i:'normal.%s.TLabel'%self._style_prefixe for i in range(7)}
  week_days[self['weekenddays'][0]-1]='we.%s.TLabel'%self._style_prefixe
  week_days[self['weekenddays'][1]-1]='we.%s.TLabel'%self._style_prefixe
  _,week_nb,d=self._date.isocalendar()
  if d==7 and self['firstweekday']=='sunday':week_nb+=1
  modulo=max(week_nb,52)
  for i_week in range(6):
   if i_week==0 or cal[i_week][0][0]:self._week_nbs[i_week].configure(text=str((week_nb+i_week-1)%modulo+1))
   else:self._week_nbs[i_week].configure(text='')
   for i_day in range(7):
    day_number,_=cal[i_week][i_day]
    style=week_days[i_day]
    label=self._calendar[i_week][i_day]
    label.state(['!disabled'])
    if day_number:
     label.configure(text=str(day_number),style=style)
     date=datetime(year,month,day_number)
     if date in self._calevent_dates:
      ev_ids=self._calevent_dates[date]
      i=len(ev_ids)-1
      while i>=0 and not self.calevents[ev_ids[i]]['tags']:i-=1
      if i>=0:
       label.configure(style='tag_%s.%s.TLabel'%(self.calevents[ev_ids[i]]['tags'][-1],self._style_prefixe))
      self.tooltip_wrapper.add_tooltip(label,'\n'.join(['➢ {}'.format(self.calevents[ev]['text']) for ev in ev_ids]))
    else:label.configure(text='',style=style)
 def _display_days_with_othermonthdays(self):
  year,month=self._date.year,self._date.month
  cal,next_m,y=self._cal.monthdatescalendar(year,month),month+1,year
  if next_m==13:
   next_m=1
   y+=1
  if len(cal)<6:
   i=0 if cal[-1][-1].month==month else 1
   cal.append(self._cal.monthdatescalendar(y,next_m)[i])
   if len(cal)<6:cal.append(self._cal.monthdatescalendar(y,next_m)[i+1])
  week_days={i:'normal' for i in range(7)}
  week_days[self.weekenddays[0]-1]='we'
  week_days[self.weekenddays[1]-1]='we'
  prev_m=(month-2)%12+1
  months={month:'.%s.TLabel'%self._style_prefixe,next_m:'_om.%s.TLabel'%self._style_prefixe,prev_m:'_om.%s.TLabel'%self._style_prefixe}
  week_nb=cal[0][1].isocalendar()[1]
  modulo=max(week_nb,52)
  for i_week in range(6):
   self._week_nbs[i_week].configure(text=str((week_nb+i_week-1)%modulo+1))
   for i_day in range(7):
    label=self._calendar[i_week][i_day]
    label.state(['!disabled'])
    label.configure(text=str(cal[i_week][i_day].day),style=week_days[i_day]+months[cal[i_week][i_day].month])
    if cal[i_week][i_day] in self._calevent_dates:
     ev_ids=self._calevent_dates[cal[i_week][i_day]]
     i=len(ev_ids)-1
     while i>=0 and not self.calevents[ev_ids[i]]['tags']:i-=1
     if i>=0:
      tag=self.calevents[ev_ids[i]]['tags'][-1]
      label.configure(style='tag_%s.%s.TLabel'%(tag,self._style_prefixe))
     text='\n'.join(['➢ {}'.format(self.calevents[ev]['text']) for ev in ev_ids])
     self.tooltip_wrapper.add_tooltip(label,text)
 def _get_day_coords(self,date):
  y1,y2,m1,m2=date.year,self._date.year,date.month,self._date.month
  if y1==y2 or(y1-y2==1 and m1==1 and m2==12)or(y2-y1==1 and m2==1 and m1==12):
   _,w,d=date.isocalendar()
   _,wn,dn=self._date.isocalendar()
   if self['firstweekday']=='sunday':
    d%=7
    if d==0:w+=1
    if dn==7:wn+=1
   else:d-=1
   w-=wn
   w %=max(52,wn)
   if 0<=w<6:return w,d
   else:return None,None
  else:return None,None
 def _display_selection(self):
  if self._sel_date!=None:
   w,d=self._get_day_coords(self._sel_date)
   if w!=None:
    label=self._calendar[w][d]
    if label.cget('text'):label.configure(style='sel.%s.TLabel'%self._style_prefixe)
 def _reset_day(self,date):
  month=date.month
  w,d=self._get_day_coords(date)
  if w!=None:
   self.tooltip_wrapper.remove_tooltip(self._calendar[w][d])
   week_end=[0,6] if self['firstweekday']=='sunday' else [5,6]
   if month==date.month:
    if d in week_end:self._calendar[w][d].configure(style='we.%s.TLabel'%self._style_prefixe)
    else:self._calendar[w][d].configure(style='normal.%s.TLabel'%self._style_prefixe)
   else:
    if d in week_end:self._calendar[w][d].configure(style='we_om.%s.TLabel'%self._style_prefixe)
    else:self._calendar[w][d].configure(style='normal_om.%s.TLabel'%self._style_prefixe)
 def _remove_selection(self):
  if self._sel_date!=None:
   if self._sel_date in self._calevent_dates:self._show_event(self._sel_date)
   else:
    w,d=self._get_day_coords(self._sel_date)
    if w!=None:
     week_end=[0,6] if self['firstweekday']=='sunday' else [5,6]
     if self._sel_date.month==self._date.month:
      if d in week_end:self._calendar[w][d].configure(style='we.%s.TLabel'%self._style_prefixe)
      else:self._calendar[w][d].configure(style='normal.%s.TLabel'%self._style_prefixe)
     else:
      if d in week_end:self._calendar[w][d].configure(style='we_om.%s.TLabel'%self._style_prefixe)
      else:self._calendar[w][d].configure(style='normal_om.%s.TLabel'%self._style_prefixe)
 def _show_event(self,date):
  w,d=self._get_day_coords(date)
  if w!=None:
   label=self._calendar[w][d]
   if not label.cget('text'):return
   ev_ids=self._calevent_dates[date]
   i=len(ev_ids)-1
   while i>=0 and not self.calevents[ev_ids[i]]['tags']:i-=1
   if i>=0:
    tag=self.calevents[ev_ids[i]]['tags'][-1]
    label.configure(style='tag_%s.%s.TLabel'%(tag,self._style_prefixe))
   text='\n'.join(['➢ {}'.format(self.calevents[ev]['text']) for ev in ev_ids])
   self.tooltip_wrapper.remove_tooltip(label)
   self.tooltip_wrapper.add_tooltip(label,text)
 def check_date_range(self,date):
  maxdate=self['maxdate']
  mindate=self['mindate']
  if maxdate!=None and date>maxdate:return maxdate
  elif mindate!=None and date<mindate:return mindate
  else:return date
 def _check_sel_date(self):
  if self._sel_date!=None:
   maxdate=self['maxdate']
   mindate=self['mindate']
   if maxdate!=None and self._sel_date>maxdate:
    self._sel_date=maxdate
    self._display_selection()
   elif mindate!=None and self._sel_date<mindate:
    self._sel_date=mindate
    self._display_selection()
 def _btns_date_range(self):
  maxdate=self['maxdate']
  mindate=self['mindate']
  if maxdate!=None:
   max_year,max_month=maxdate.year,maxdate.month
   if self._date>maxdate:
    self._date=self._date.replace(year=max_year,month=max_month)
    self._display_calendar()
   dy=max_year-self._date.year
   if dy==0:
    self._r_year.state(['disabled'])
    if self._date.month==max_month:self._r_month.state(['disabled'])
    else:self._r_month.state(['!disabled'])
   elif dy==1:
    if self._date.month>max_month:self._r_year.state(['disabled'])
    else:
     self._r_year.state(['!disabled'])
     self._r_month.state(['!disabled'])
   else:
    self._r_year.state(['!disabled'])
    self._r_month.state(['!disabled'])
  if mindate!=None:
   min_year,min_month=mindate.year,mindate.month
   if self._date<mindate:
    self._date=self._date.replace(year=min_year,month=min_month)
    self._display_calendar()
   dy=self._date.year-min_year
   if dy==0:
    self._l_year.state(['disabled'])
    if self._date.month==min_month:self._l_month.state(['disabled'])
    else:self._l_month.state(['!disabled'])
   elif dy==1:
    if self._date.month>=min_month:
     self._l_year.state(['!disabled'])
     self._l_month.state(['!disabled'])
    else:self._l_year.state(['disabled'])
   else:
    self._l_year.state(['!disabled'])
    self._l_month.state(['!disabled'])
 def _next_month(self):
  year,month=self._date.year,self._date.month
  self._date=self._date+timedelta(days=monthrange(year,month)[1])
  self._display_calendar()
  self.event_generate('<<CalendarMonthChanged>>')
  self._btns_date_range()
 def _prev_month(self):
  self._date=self._date-timedelta(days=1)
  self._date=self._date.replace(day=1)
  self._display_calendar()
  self.event_generate('<<CalendarMonthChanged>>')
  self._btns_date_range()
 def _next_year(self):
  year=self._date.year
  self._date=self._date.replace(year=year+1)
  self._display_calendar()
  self.event_generate('<<CalendarMonthChanged>>')
  self._btns_date_range()
 def _prev_year(self):
  year=self._date.year
  self._date=self._date.replace(year=year-1)
  self._display_calendar()
  self.event_generate('<<CalendarMonthChanged>>')
  self._btns_date_range()
 def _on_click(self,event):
  if self._properties['state']=='normal':
   label=event.widget
   if 'disabled' not in label.state():
    day,style=label.cget('text'),label.cget('style')
    if style in ['normal_om.%s.TLabel'%self._style_prefixe,'we_om.%s.TLabel'%self._style_prefixe]:
     if label in self._calendar[0]:self._prev_month()
     else:self._next_month()
    if day:
     day,year,month=int(day),self._date.year,self._date.month
     self._remove_selection()
     self._sel_date=datetime(year,month,day)
     self._display_selection()
     if self._textvariable!=None:self._textvariable.set(self.format_date(self._sel_date))
     self.event_generate('<<CalendarSelected>>')
 def _get_date_pattern(self,date_pattern,locale=None):
  if locale==None:locale=self._properties['locale']
  if date_pattern=='short':return get_date_format('short',locale).pattern
  pattern=date_pattern.lower()
  if ((search(r'^y+[^a-zA-Z]*m{1,2}[^a-z]*d{1,2}[^mdy]*$',pattern)!=None) or (search(r'^m{1,2}[^a-zA-Z]*d{1,2}[^a-z]*y+[^mdy]*$',pattern)!=None) or (search(r'^d{1,2}[^a-zA-Z]*m{1,2}[^a-z]*y+[^mdy]*$',pattern)!=None)):
   return pattern.replace('m','M')
  raise ValueError(f'{date_pattern}は有効な日付パターンではありません')
 def format_date(self,date=None):return format_date(date,self._properties['date_pattern'],self._properties['locale'])
 def parse_date(self,date):
  date_format=self._properties['date_pattern'].lower()
  year_idx=date_format.index('y')
  month_idx=date_format.index('m')
  day_idx=date_format.index('d')
  indexes=[(year_idx,'Y'),(month_idx,'M'),(day_idx,'D')]
  indexes.sort()
  indexes=dict([(item[1],idx) for idx,item in enumerate(indexes)])
  numbers=findall(r'(\d+)',date)
  year=numbers[indexes['Y']]
  year=2000+int(year) if len(year)==2 else int(year)
  month=int(numbers[indexes['M']])
  day=int(numbers[indexes['D']])
  if month>12:month,day=day,month
  return datetime(year,month,day)
 def see(self,date):
  if isinstance(date,datetime):date=date.date()
  elif not isinstance(date,datetime):
   raise TypeError('date引数にはdatetimeを指定してください')
  self._date=self._date.replace(month=date.month,year=date.year)
  self._display_calendar()
  self._btns_date_range()
 def selection_clear(self):
  self._remove_selection()
  self._sel_date=None
  if self._textvariable!=None:self._textvariable.set('')
 def selection_get(self):return self._sel_date if self._properties.get('selectmode')=='day' else None
 def selection_set(self,date):
  if self._properties.get('selectmode')=='day' and self._properties['state']=='normal':
   if date==None:self.selection_clear()
   else:
    if isinstance(date,datetime):self._sel_date=date.date()
    elif isinstance(date,datetime):self._sel_date=date
    else:
     try:self._sel_date=self.parse_date(date)
     except Exception:
      raise ValueError(f'{date}は有効な日付ではありません')
    if self['mindate']!=None and self._sel_date<self['mindate']:self._sel_date=self['mindate']
    elif self['maxdate']!=None and self._sel_date>self['maxdate']:self._sel_date=self['maxdate']
    if self._textvariable!=None:self._textvariable.set(self.format_date(self._sel_date))
    self._date=self._sel_date.replace(day=1)
    self._display_calendar()
    self._display_selection()
    self._btns_date_range()
 def get_displayed_month(self):return self._date.month,self._date.year
 def get_date(self):return self.format_date(self._sel_date) if self._sel_date!=None else ''
 def calevent_create(self,date,text,tags=[]):
  if isinstance(date,datetime):date=date.date()
  if not isinstance(date,Calendar.date):
   raise TypeError('date option should be a %s instance'%(Calendar.date))
  ev_id=max(self.calevents)+1 if self.calevents else 0
  tags_=[tags] if isinstance(tags,str) else list(tags)
  self.calevents[ev_id]={'date':date,'text':text,'tags':tags_}
  for tag in tags_:
   if tag not in self._tags:self._tag_initialize(tag)
  if date not in self._calevent_dates:self._calevent_dates[date]=[ev_id]
  else:self._calevent_dates[date].append(ev_id)
  self._show_event(date)
  return ev_id
 def _calevent_remove(self,ev_id):
  try:date=self.calevents[ev_id]['date']
  except KeyError:ValueError('event %s does not exists'%ev_id)
  else:
   del self.calevents[ev_id]
   self._calevent_dates[date].remove(ev_id)
   if not self._calevent_dates[date]:
    del self._calevent_dates[date]
    self._reset_day(date)
   else:self._show_event(date)
 def calevent_remove(self,*ev_ids,**kw):
  if ev_ids:
   if 'all' in ev_ids:ev_ids=self.get_calevents()
   for ev_id in ev_ids:self._calevent_remove(ev_id)
  else:
   for ev_id in self.get_calevents(tag=kw.get('tag'),date=kw.get('date')):self._calevent_remove(ev_id)
 def calevent_cget(self,ev_id,option):
  try:ev=self.calevents[ev_id]
  except KeyError:
   raise ValueError('event %s does not exists'%ev_id)
  else:
   try:return ev[option]
   except KeyError:
    raise ValueError('unknown option \'%s\''%option)
 def calevent_configure(self,ev_id,**kw):
  try:ev=self.calevents[ev_id]
  except KeyError:
   raise ValueError('event %s does not exists'%ev_id)
  else:
   text,tags,date=kw.get('text'),kw.get('tags'),kw.get('date')
   if kw:
    raise KeyError('Invalid keyword option(s) %s,valid options are \'text\',\'tags\' and \'date\'.'%(kw.keys(),))
   else:
    if text!=None:ev['text']=str(text)
    if tags!=None:
     if isinstance(tags,str):tags_=[tags]
     else:tags_=list(tags)
     for tag in tags_:
      if tag not in self._tags:self._tag_initialize(tag)
     ev['tags']=tags_
    if date!=None:
     if isinstance(date,self.datetime):date=date.date()
     if not isinstance(date,self.date):
      raise TypeError('date option should be a %s instance'%(self.date))
     old_date=ev['date']
     self._calevent_dates[old_date].remove(ev_id)
     if self._calevent_dates[old_date]:self._show_event(old_date)
     else:self._reset_day(old_date)
     ev['date']=date
     if date in self._calevent_dates:self._calevent_dates[date].append(ev_id)
     else:self._calevent_dates[date]=[ev_id]
    self._show_event(ev['date'])
 def calevent_raise(self,ev_id,above=None):
  try:date=self.calevents[ev_id]['date']
  except KeyError:
   raise ValueError('event %s does not exists'%ev_id)
  else:
   evs=self._calevent_dates[date]
   if above==None:
    evs.remove(ev_id)
    evs.insert(0,ev_id)
   else:
    if above not in evs:
     raise ValueError('event %s does not exists on %s'%(above,date))
    else:
     evs.remove(ev_id)
     index=evs.index(above)
     evs.insert(index,ev_id)
   self._show_event(date)
 def calevent_lower(self,ev_id,below=None):
  try:date=self.calevents[ev_id]['date']
  except KeyError:
   raise ValueError('event %s does not exists'%ev_id)
  else:
   evs=self._calevent_dates[date]
   if below==None:
    evs.remove(ev_id)
    evs.append(ev_id)
   else:
    if below not in evs:
     raise ValueError('event %s does not exists on %s'%(below,date))
    else:
     evs.remove(ev_id)
     index=evs.index(below)+1
     evs.insert(index,ev_id)
   self._show_event(date)
 def get_calevents(self,date=None,tag=None):
  if date!=None:
   if isinstance(date,Calendar.datetime):date=date.date()
   if not isinstance(date,Calendar.date):
    raise TypeError('date option should be a %s instance'%(Calendar.date))
   try:return tuple(ev_id for ev_id in self._calevent_dates[date] if tag in self.calevents[ev_id]['tags']) if tag!=None else tuple(self._calevent_dates[date])
   except KeyError:return()
  elif tag!=None:return tuple(k for k,v in self.calevents.items() if tag in v['tags'])
  else:return tuple(self.calevents.keys())
 def _tag_initialize(self,tag):
  props=dict(foreground='white',background='royal blue')
  self._tags[tag]=props
  self.style.configure('tag_%s.%s.TLabel'%(tag,self._style_prefixe),**props)
 def tag_config(self,tag,**kw):
  if tag not in self._tags:self._tags[tag]={}
  props=dict(foreground='white',background='royal blue')
  props.update(self._tags[tag])
  props.update(kw)
  self.style.configure('tag_%s.%s.TLabel'%(tag,self._style_prefixe),**props)
  self._tags[tag]=props
 def tag_cget(self,tag,option):
  try:prop=self._tags[tag]
  except KeyError:
   raise ValueError('unknow tag \'%s\''%tag)
  else:
   try:return prop[option]
   except KeyError:
    raise ValueError('unknow option \'%s\''%option)
 def tag_names(self):return tuple(self._tags.keys())
 def tag_delete(self,tag):
  try:del self._tags[tag]
  except KeyError:
   raise ValueError('tag \'%s\' does not exists'%tag)
  else:
   for props in self.calevents.values():
    if tag in props['tags']:props['tags'].remove(tag)
   self._display_calendar()
 def keys(self):return list(self._properties.keys())
 def cget(self,key):return self[key]
 def configure(self,cnf={},**kw):
  if not isinstance(cnf,dict):
   raise TypeError('Expected a dictionary or keyword arguments.')
  kw=cnf.copy()
  kw.update(kw)
  for k,v in kw.items():self[k]=v
 config=configure