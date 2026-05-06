from tkinter import (BooleanVar, Button, Checkbutton, Entry, Frame, IntVar,
                     Label, LabelFrame, Listbox, Menu, Menubutton, Radiobutton,
                     Scale, Spinbox, StringVar, Text)
from tkinter.ttk import Notebook, Style, Treeview

from .._function import bols, listchose, num0, nums, parsecolor
from .._log import Logger
from ..base import Element

logger=Logger(name='element',format={'filename':None,'lineno':{'after':'行目'},'message':None}).get_logger()
class Texts(Element):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.wraplength=num0(kw.get('wraplength'))
  self.text=kw.get('text')
  self.widget=Label(self.master,takefocus=self.takefocus,borderwidth=self.borderwidth,anchor=self.anchor,pady=self.pady,padx=self.padx,relief=self.relief,wraplength=self.wraplength,cursor=self.cursor,text=self.text,bg=self.bg,fg=self.fg,font=self.font,width=self.width,height=self.height,justify=self.justify)
 def delta(self):
  try:self.widget.destroy()
  except Exception as e:
   logger.error(e)
 def get_text(self):
  try:
   return self.text
  except Exception as e:
   logger.error(e)
 def set_text(self,txt):
  try:
   self.text=txt
   self.widget.config(text=txt)
  except Exception as e:logger.error(e)
 def get_fg(self):
  try:return str(self.bg)
  except Exception as e:logger.error(e)
 def set_fg(self,fg):
  try:
   self.fg=fg
   self.widget.config(fg=fg)
  except Exception as e:logger.error(e)
 def get_bg(self):
  try:return str(self.bg)
  except Exception as e:logger.error(e)
 def set_bg(self,bg):
  try:
   self.bg=bg
   self.widget.config(bg=bg)
  except Exception as e:
   logger.error(e)
class Buttons(Element):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.funcs=kw.get('function')
  self.text=kw.get('text')
  self.wraplength=num0(kw.get('wraplength'))
  self.bg=parsecolor(kw.get('bg'),'#e0e0e0')
  self.anchor=listchose(kw.get('anchor'),['w','n','s','e','nw','ne','se','sw','center'],'center')
  self.widget=Button(self.master,takefocus=self.takefocus,anchor=self.anchor,pady=self.pady,padx=self.padx,relief=self.relief,wraplength=self.wraplength,cursor=self.cursor,text=self.text,bg=self.bg,fg=self.fg,font=self.font,command=lambda:self._exec_funcs(self.funcs),width=self.width,height=self.height,borderwidth=self.borderwidth)
 def delta(self):
  try:self.widget.destroy()
  except Exception as e:
   logger.error(e)
 def get_text(self):
  try:
   return self.text
  except Exception as e:
   logger.error(e)
 def set_text(self,txt):
  try:
   self.text=txt
   self.widget.config(text=txt)
  except Exception as e:logger.error(e)
 def get_fg(self):
  try:return str(self.bg)
  except Exception as e:logger.error(e)
 def set_fg(self,fg):
  try:
   self.fg=fg
   self.widget.config(fg=fg)
  except Exception as e:logger.error(e)
 def get_bg(self):
  try:return str(self.bg)
  except Exception as e:logger.error(e)
 def set_bg(self,bg):
  try:
   self.bg=bg
   self.widget.config(bg=bg)
  except Exception as e:
   logger.error(e)
class Input(Element):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.bg=parsecolor(kw.get('bg'),'#e0e0e0')
  self.width=num0(kw.get('width'),20)
  self.text=kw.get('text')
  self.show=kw.get('show')
  self.insertbackground=parsecolor(kw.get('insertbg'),'#000000')
  self.insertwidth=num0(kw.get('insertwidth'),2)
  self.widget=Entry(self.master,takefocus=self.takefocus,relief=self.relief,cursor=self.cursor,insertwidth=self.insertwidth,insertbackground=self.insertbackground,bg=self.bg,fg=self.fg,font=self.font,width=self.width,justify=self.justify,show=self.show,borderwidth=self.borderwidth)
  if self.text!=None:self.inserts(self.text)
 def inserts(self,text='',place='end'):self.widget.insert(place,text)
 def get_text(self):return self.widget.get()
 def select_judge(self):return self.widget.select_present()
 def select_cansel(self):self.widget.select_clear()
 def all_delta(self):self.widget.delete(0,'end')
 def delta(self):
  try:self.widget.destroy()
  except Exception as e:
   logger.error(e)
 def set_text(self,txt):
  try:
   self.text=txt
   self.all_delta()
   self.inserts(self.text)
  except Exception as e:logger.error(e)
 def get_fg(self):
  try:return str(self.bg)
  except Exception as e:logger.error(e)
 def set_fg(self,fg):
  try:
   self.fg=fg
   self.widget.config(fg=fg)
  except Exception as e:logger.error(e)
 def get_bg(self):
  try:return str(self.bg)
  except Exception as e:logger.error(e)
 def set_bg(self,bg):
  try:
   self.bg=bg
   self.widget.config(bg=bg)
  except Exception as e:
   logger.error(e)
class Multiline(Element):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.bg=parsecolor(kw.get('bg'),'#e0e0e0')
  self.width=self._size_width(kw.get('width'),20)
  self.height=self._size_width(kw.get('height'),5)
  self.text=kw.get('text')
  self.borderwidth=num0(kw.get('bd'),1)
  self.state=listchose(kw.get('state'),['normal','disabled'])
  self.wrap=listchose(kw.get('wrap'),['none','word','char'])
  self.insertbackground=parsecolor(kw.get('insertbg'),'#000000')
  self.insertwidth=num0(kw.get('insertwidth'),2)
  self.widget=Text(self.master,takefocus=self.takefocus,insertbackground=self.insertbackground,insertwidth=self.insertwidth,padx=self.padx,pady=self.pady,relief=self.relief,cursor=self.cursor,bg=self.bg,fg=self.fg,font=self.font,width=self.width,height=self.height,state=self.state,wrap=self.wrap,borderwidth=self.borderwidth)
  if self.text!=None:
   if isinstance(self.text,list|tuple):
    savetext=''
    lens=len(list(self.text))-1
    for i,item in enumerate(list(self.text)):savetext=(savetext+item) if i==lens else (savetext+f'{item}\n')
    self.text=savetext
    self.inserts(savetext,place='end')
   else:self.inserts(self.text,place='end')
 def inserts(self,text,place='end'):self.widget.insert(place,text)
 def get_text(self):return self.widget.get(1.0,'end-1c')
 def all_delta(self):self.widget.delete(1.0,'end')
 def delta(self):
  try:self.widget.destroy()
  except Exception as e:
   logger.error(e)
 def get_fg(self):
  try:return str(self.bg)
  except Exception as e:logger.error(e)
 def set_fg(self,fg):
  try:
   self.fg=fg
   self.widget.config(fg=fg)
  except Exception as e:logger.error(e)
 def get_bg(self):
  try:return str(self.bg)
  except Exception as e:logger.error(e)
 def set_bg(self,bg):
  try:
   self.bg=bg
   self.widget.config(bg=bg)
  except Exception as e:
   logger.error(e)
class InputNumber(Element):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.bg=parsecolor(kw.get('bg'),'#e0e0e0')
  self.min=nums(kw.get('min'),0)
  self.max=nums(kw.get('max'),100)
  self.increment=num0(kw.get('step'),1)
  self.wrap=bols(kw.get('wrap'),False)
  self.width=num0(kw.get('width'),20)
  self.insertbackground=parsecolor(kw.get('insertbg'),'#000000')
  self.insertwidth=num0(kw.get('insertwidth'),2)
  self.values=nums(kw.get('values'),0)
  self.intval=IntVar(value=self.values)
  self.widget=Spinbox(self.master,textvariable=self.intval,takefocus=self.takefocus,insertbackground=self.insertbackground,insertwidth=self.insertwidth,relief=self.relief,cursor=self.cursor,from_=self.min,to=self.max,increment=self.increment,bg=self.bg,fg=self.fg,font=self.font,justify=self.justify,wrap=self.wrap,width=self.width,borderwidth=self.borderwidth)
 def get_number(self):return self.widget.get()
 def delta(self):
  try:self.widget.destroy()
  except Exception as e:
   logger.error(e)
 def get_fg(self):
  try:return str(self.bg)
  except Exception as e:logger.error(e)
 def set_fg(self,fg):
  try:
   self.fg=fg
   self.widget.config(fg=fg)
  except Exception as e:logger.error(e)
 def get_bg(self):
  try:return str(self.bg)
  except Exception as e:logger.error(e)
 def set_bg(self,bg):
  try:
   self.bg=bg
   self.widget.config(bg=bg)
  except Exception as e:
   logger.error(e)
class Listboxs(Element):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.values=kw.get('values') if isinstance(kw.get('values'),tuple|list) else []
  self.bg=parsecolor(kw.get('bg'),'#e0e0e0')
  self.selectforeground=parsecolor(kw.get('selectfg'),'#000000')
  self.selectbackground=parsecolor(kw.get('selectbg'),'#1967d2')
  self.exportselection=bols(kw.get('exportselection'),False)
  self.selectmode=listchose(kw.get('selectmode'),['browse','single','multiple','extended'])
  self.width=self._size_width(kw.get('width'),20)
  self.height=self._size_height(kw.get('height'),min(max(len(self.values),1),5))
  self.state=listchose(kw.get('state'),['normal','disabled'])
  self.widget=Listbox(self.master,exportselection=self.exportselection,selectforeground=self.selectforeground,selectbackground=self.selectbackground,relief=self.relief,cursor=self.cursor,listvariable=StringVar(value=self.values),bg=self.bg,fg=self.fg,font=self.font,selectmode=self.selectmode,width=self.width,height=self.height,justify=self.justify,state=self.state,borderwidth=self.borderwidth)
  self.selectval=nums(kw.get('select'),0)
  self.select_set(self.selectval)
 def select_set(self,val):
  if isinstance(val,int):
   if val<0:val=0
   elif len(self.values)<val:val=len(self.values)-1
   self.widget.selection_set(val)
 def apend(self,lists=[],place='end'):
  if isinstance(lists,list|tuple):
   for i in lists:self.widget.insert(place,i)
 def clear(self):self.widget.delete(0,'end')
 def dele(self,*index):
  if isinstance(index,tuple):
   for i in index:
    if isinstance(i,int)and not(i<0 or self.lens()<i):self.widget.delete(i)
 def lens(self):return self.widget.size()
 def select(self):return self.widget.curselection()
 def select_val(self):
  val=list(self.widget.curselection())
  if len(val)==1:return self.values[val[0]]
  elif len(val)==0:return None
  else:return[self.values[i] for i in val]
 def set(self,lists):
  if isinstance(lists,list|tuple):
   self.clear()
   self.apend(lists,'end')
 def delta(self):
  try:self.widget.destroy()
  except Exception as e:
   logger.error(e)
 def get_fg(self):
  try:return str(self.bg)
  except Exception as e:logger.error(e)
 def set_fg(self,fg):
  try:
   self.fg=fg
   self.widget.config(fg=fg)
  except Exception as e:logger.error(e)
 def get_bg(self):
  try:return str(self.bg)
  except Exception as e:logger.error(e)
 def set_bg(self,bg):
  try:
   self.bg=bg
   self.widget.config(bg=bg)
  except Exception as e:
   logger.error(e)
class Radio(Element):
 groups,text_list,count={},{},0
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.count+=1
  self.wraplength=num0(kw.get('wraplength'))
  self.group=kw.get('group','default')
  self.text=kw.get('text')
  self._count(self.text)
  self.value=f'{self.text}{self.text_list.get(self.text)}'
  if self.groups.get(self.group)==None:self.groups[self.group]={'var':StringVar(),'has_default':False,'text':self.text}
  group_data=self.groups[self.group]
  self.variable=group_data['var']
  self.widget=Radiobutton(self.master,variable=self.variable,bg=self.bg,fg=self.fg,font=self.font,takefocus=self.takefocus,anchor=self.anchor,pady=self.pady,padx=self.padx,relief=self.relief,wraplength=self.wraplength,cursor=self.cursor,text=self.text,value=self.value,borderwidth=self.borderwidth)
  if not group_data['has_default']:
   self.variable.set(self.value)
   group_data['has_default']=True
 def _count(self,val):self.text_list[val]=1 if self.text_list.get(val)==None else self.text_list[val]+1
 def delta(self):
  try:self.widget.destroy()
  except Exception as e:
   logger.error(e)
 def get_text(self):
  try:
   return self.text
  except Exception as e:
   logger.error(e)
 def set_text(self,txt):
  try:
   self.text=txt
   self.widget.config(text=txt)
  except Exception as e:logger.error(e)
 def get_fg(self):
  try:return str(self.bg)
  except Exception as e:logger.error(e)
 def set_fg(self,fg):
  try:
   self.fg=fg
   self.widget.config(fg=fg)
  except Exception as e:logger.error(e)
 def get_bg(self):
  try:return str(self.bg)
  except Exception as e:logger.error(e)
 def set_bg(self,bg):
  try:
   self.bg=bg
   self.widget.config(bg=bg)
  except Exception as e:
   logger.error(e)
class Checkbox(Element):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.wraplength=num0(kw.get('wraplength'))
  self.text=kw.get('text')
  self.default=bols(kw.get('default'),False)
  self.variable=BooleanVar()
  self.widget=Checkbutton(self.master,takefocus=self.takefocus,anchor=self.anchor,pady=self.pady,padx=self.padx,relief=self.relief,wraplength=self.wraplength,cursor=self.cursor,text=self.text,variable=self.variable,bg=self.bg,fg=self.fg,font=self.font,borderwidth=self.borderwidth)
  if self.default:
   self.widget.select()
   self.variable.set(True)
  else:
   self.widget.deselect()
   self.variable.set(False)
 def get_value(self):return self.variable.get()
 def set_value(self,value=None):self.variable.set(value if isinstance(value,bool) else (not self.variable.get()))
 def delta(self):
  try:self.widget.destroy()
  except Exception as e:
   logger.error(e)
 def get_text(self):
  try:
   return self.text
  except Exception as e:
   logger.error(e)
 def set_text(self,txt):
  try:
   self.text=txt
   self.widget.config(text=txt)
  except Exception as e:logger.error(e)
 def get_fg(self):
  try:return str(self.bg)
  except Exception as e:logger.error(e)
 def set_fg(self,fg):
  try:
   self.fg=fg
   self.widget.config(fg=fg)
  except Exception as e:logger.error(e)
 def get_bg(self):
  try:return str(self.bg)
  except Exception as e:logger.error(e)
 def set_bg(self,bg):
  try:
   self.bg=bg
   self.widget.config(bg=bg)
  except Exception as e:
   logger.error(e)
class Tree(Element):
 sums=1
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.colwidth=kw.get('colwidth',120)
  self.bg=parsecolor(kw.get('bg'),'#e0e0e0')
  self.header_fg=parsecolor(kw.get('header_fg'),'#000000')
  self.header_bg=parsecolor(kw.get('header_bg'),'#cccccc')
  self.rowheight=kw.get('rowheight',50)
  if not isinstance(kw.get('values',[]),list):
   raise TypeError('valuesにlist型を指定してください。')
  else:self.values=kw.get('values',[])
  if not isinstance(kw.get('header',[]),list):
   raise TypeError('headerにlist型を指定してください。')
  else:self.header=kw.get('header',[])
  self.side_header=kw.get('side_header')
  self.maxcols=1 if self._calc_max_columns(self.values)<1 else self._calc_max_columns(self.values)
  cols=[f'col{i}' for i in range(1,self.maxcols+1)]
  self.widget=Treeview(self.master,columns=cols,show='tree' if self.header==[] else 'tree headings')
  if self.header!=[] and len(self.header)<self.maxcols:
   for i in range(self.maxcols-len(self.header)):self.header.append('')
  self.widget.heading('#0',text=self.side_header)
  self.widget.column('#0',width=200,anchor='w')
  for i,c in enumerate(cols):
   self.widget.heading(c,text='' if self.header==[] else self.header[i])
   self.widget.column(c,width=self.colwidth,anchor='w')
  style=Style()
  self.stylename=f'Tree{kw.get('count')}.Treeview'
  style.configure(style=f'{self.stylename}.Heading',background=self.header_bg,foreground=self.header_fg,font=self.font)
  self.widget.configure(style=f'{self.stylename}.Heading')
  style.configure(style=self.stylename,background=self.bg,foreground=self.fg,fieldbackground=self.bg,font=self.font,rowheight=self.rowheight)
  self.widget.configure(style=self.stylename)
  self.widget.grid_rowconfigure(0,weight=1)
  self.widget.grid_columnconfigure(0,weight=1)
  self._build_from_values(self.values)
  self.widget.config(height=min(num0(self.sums,1),15))
 def _calc_max_columns(self,vals):
  maxc,i,L=0,0,len(vals)
  while i<L:
   v=vals[i]
   if isinstance(v,str)and i+1<L and isinstance(vals[i+1],list):
     c=self._maxlen_in_list(vals[i+1])
     if maxc<c:maxc=c
     i+=2
   else:i+=1
  return maxc
 def _maxlen_in_list(self,lst):
  maxc,strings=0,[x for x in lst if not isinstance(x,list)]
  if maxc<len(strings):maxc=len(strings)
  for x in lst:
   if isinstance(x,list):
    c=self._maxlen_in_list(x)
    if maxc<c:maxc=c
  return maxc
 def _flatten_strings(self,lst):
  out=[]
  for x in lst:
   if isinstance(x,list):out.extend(self._flatten_strings(x))
   else:out.append(x)
  return out
 def _build_from_values(self,vals):
  i,L=0,len(vals)
  while i<L:
   item=vals[i]
   if isinstance(item,str)and i+1<L and isinstance(vals[i+1],list):
     self._process_data_list(self.widget.insert('','end',text=item,values=('')*self.maxcols),item,vals[i+1])
     self.sums+=2
     i+=2
   else:
    self.sums+=1
    i+=1
 def _process_data_list(self,parent_id,parent_text,data_list):
  summary_values=[x for x in data_list if not isinstance(x,list)]
  summary_id=self.widget.insert(parent_id,'end',text=parent_text,values=(tuple((str(x) for x in summary_values[:self.maxcols]))+tuple('' for _ in range(max(0,self.maxcols-len(summary_values))))))
  for idx,x in enumerate(data_list):
   if isinstance(x,list):
    k,dk=idx-1,data_list[k]
    while k<=0 and isinstance(dk,list):k-=1
    label=dk if 0<=k and isinstance(dk,str) else ''
    if any(isinstance(s,list) for s in x):
     nesumval=[s for s in x if not isinstance(s,list)]
     for y in x:
      if isinstance(y,list):self._process_data_list(self.widget.insert(summary_id,'end',text=label,values=tuple((str(s) for s in nesumval[:self.maxcols]))+tuple('' for _ in range(max(0,self.maxcols-len(nesumval))))),label,y)
    else:self.widget.insert(summary_id,'end',text=label,values=tuple((str(s) for s in x[:self.maxcols]))+tuple('' for _ in range(max(0,self.maxcols-len(x)))))
 def _get_iid(self,item=None):
  for child in self.widget.get_children(item):
   yield child
   yield from self._get_iid(child)
 def get_iid(self):return list(self._get_iid())
 def expand(self,iid):self.widget.item(iid,open=True)
 def collapse(self,iid):self.widget.item(iid,open=False)
 def get_path(self,iid):
  parts,cur=[],iid
  while cur:
   txt=self.widget.item(cur,'text')
   if txt:parts.append(txt)
   cur=self.widget.parent(cur)
  parts.reverse()
  return '/'.join(parts)
 def add_node(self,parent_iid,text,data_list=None):
  pid=self.widget.insert(parent_iid,'end',text=text,values=('')*self.maxcols)
  if isinstance(data_list,list):self._process_data_list(pid,text,data_list)
  return pid
 def delete_node(self,iid):self.widget.delete(iid)
 def clear_width(self):
  columns=self.widget['columns']
  self.widget.update_idletasks()
  if 0<len(columns):
   for col in columns:self.widget.column(col,width=int(self.widget.winfo_width()/len(columns)))
 def delta(self):
  try:self.widget.destroy()
  except Exception as e:
   logger.error(e)
class Table(Element):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.header_fg=parsecolor(kw.get('header_fg'),'#000000')
  self.bg=parsecolor(kw.get('bg'),'#e0e0e0')
  self.header_bg=parsecolor(kw.get('header_bg'),'#cccccc')
  self.values=kw.get('values',[])
  self.header=kw.get('header',[])
  self.colwidth=kw.get('colwidth',120)
  self.height=kw.get('height',max(len(self.values),1))
  self.rowheight=kw.get('rowheight',50)
  self.rowheader=kw.get('rowheader',[])
  self.stylename=f'Table{kw.get('count')}.Treeview'
  self.widget=Treeview(self.master,show='headings',style=self.stylename,height=self.height,takefocus=self.takefocus)
  style=Style()
  style.configure(style=f'{self.stylename}.Heading',background=self.header_bg,foreground=self.header_fg,font=self.font)
  self.widget.configure(style=f'{self.stylename}.Heading')
  style.configure(style=self.stylename,background=self.bg,foreground=self.fg,fieldbackground=self.bg,font=self.font,rowheight=self.rowheight)
  self.widget.configure(style=self.stylename)
  columns=[]
  if self.rowheader:columns.append('rowheader')
  if self.header:columns+=self.header
  else:
   if 0<len(self.values):columns+=[f'col_{str(i)}' for i in range(len(self.values[0]))]
  self.widget['columns']=columns
  rows=(' ' if self.rowheader else '行')
  for col in columns:
   self.widget.heading(col,text=rows if col=='rowheader' else col if self.header else '')
   self.widget.column(col,anchor='center',width=self.colwidth)
  self.widget.tag_configure('rowheader_tag',background=self.header_bg,foreground=self.header_fg)
  if self.rowheader:
   for i,row in enumerate(self.values):self.widget.item(self.widget.insert('','end',values=[self.rowheader[i] if i<len(self.rowheader) else '']+row),tags=('rowheader_tag'))
  else:
   for row in self.values:self.widget.insert('','end',values=row)
  self.widget.grid_rowconfigure(0,weight=1)
  self.widget.grid_columnconfigure(0,weight=1)
 def clear_width(self,total_width=None):
  columns=self.widget['columns']
  if total_width==None:
   self.widget.update_idletasks()
   total_width=self.widget.winfo_width()
  width=int(total_width/len(columns))
  if 0<len(columns):
   for col in columns:self.widget.column(col,width=width)
 def delta(self):
  try:self.widget.destroy()
  except Exception as e:
   logger.error(e)
class Slidebar(Element):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.value=num0(kw.get('value'))
  self.minval=num0(kw.get('min'))
  self.maxval=self.value if kw.get('max',100)<self.value else kw.get('max')
  self.orientation=listchose(kw.get('orientation'),['horizontal','vertical'],'horizontal')
  self.resolution=num0(kw.get('resolution'),1)
  self.digits=num0(kw.get('digits'))
  self.length=num0(kw.get('length'),200)
  self.borderwidth=num0(kw.get('bd'),1)
  self.widget=Scale(self.master,takefocus=self.takefocus,relief=self.relief,cursor=self.cursor,fg=self.fg,bg=self.bg,font=self.font,from_=self.minval,to=self.maxval,orient=self.orientation,resolution=self.resolution,digits=self.digits,length=self.length,borderwidth=self.borderwidth)
  self.set(self.value)
 def set(self,val):
  if nums(val):self.widget.set(val)
 def _get(self):return self.widget.get()
 def delta(self):
  try:self.widget.destroy()
  except Exception as e:
   logger.error(e)
 def get_fg(self):
  try:return str(self.bg)
  except Exception as e:logger.error(e)
 def set_fg(self,fg):
  try:
   self.fg=fg
   self.widget.config(fg=fg)
  except Exception as e:logger.error(e)
 def get_bg(self):
  try:return str(self.bg)
  except Exception as e:logger.error(e)
 def set_bg(self,bg):
  try:
   self.bg=bg
   self.widget.config(bg=bg)
  except Exception as e:
   logger.error(e)
class Menus(Element):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.menu_lists=kw.get('list',[])
  self.funcs=None
  self.tearoff=bols(kw.get('tearoff'),False)
  self.widget:Menu=Menu(self.master,takefocus=self.takefocus,relief=self.relief,cursor=self.cursor,tearoff=self.tearoff,bg=self.bg,fg=self.fg,font=self.font,borderwidth=self.borderwidth)
  self._create_menu_lists()
 def _create_menu_lists(self):
  self.widget.delete(0,'end')
  for menus in self.menu_lists:
   if not isinstance(menus,list):continue
   for i in range(0,len(menus),2):
    if len(menus)<=i+1:break
    submenu=Menu(self.widget,tearoff=self.tearoff,bg=self.bg,fg=self.fg,font=self.font)
    self._add_items_recursive(menu=submenu,items=menus[i+1])
    self.widget.add_cascade(label=menus[i],menu=submenu)
 def _add_items_recursive(self,menu:Menu,items):
  i=0
  while i<len(items):
   item=items[i]
   if item=='---':
    menu.add_separator()
    i+=1
    continue
   if isinstance(item,dict):
    self.funcs=item.get('function')
    if self.funcs:menu.add_command(label=item.get('label',''),command=lambda f=self.funcs:self._exec_funcs(f))
    else:menu.add_command(label=item.get('label',''))
    i+=1
    continue
   if isinstance(item,str):
    if i+1<len(items) and isinstance(items[i+1],list):
     new_sub=Menu(menu,tearoff=self.tearoff,bg=self.bg,fg=self.fg,font=self.font)
     self._add_items_recursive(new_sub,items[i+1])
     menu.add_cascade(label=item,menu=new_sub)
     i+=2
     continue
    else:
     menu.add_command(label=item)
     i+=1
     continue
   if isinstance(item,list):
    new_sub=Menu(menu,tearoff=self.tearoff,bg=self.bg,fg=self.fg,font=self.font)
    self._add_items_recursive(new_sub,item)
    menu.add_cascade(label='Submenu',menu=new_sub)
    i+=1
    continue
 def get(self):return self.menu_lists
 def clear(self):
  self.widget.delete(0,'end')
  self.menu_lists=[]
 def addmenu(self,label,submenu_lists):
  self.menu_lists.append([label,submenu_lists])
  self._create_menu_lists()
 def delta(self):
  try:self.widget.destroy()
  except Exception as e:
   logger.error(e)
 def get_bg(self):
  try:return str(self.bg)
  except Exception as e:logger.error(e)
 def set_bg(self,bg):
  try:
   self.bg=bg
   self.widget.config(bg=bg)
  except Exception as e:
   logger.error(e)
class Menubuttons(Element):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.bg=parsecolor(kw.get('bg'),'#e0e0e0')
  self.text=kw.get('text')
  self.menu_lists=kw.get('list',[])
  self.tearoff=bols(kw.get('tearoff'),False)
  self.widget=Menubutton(self.master,takefocus=self.takefocus,anchor=self.anchor,pady=self.pady,padx=self.padx,relief=self.relief,cursor=self.cursor,text=self.text,bg=self.bg,fg=self.fg,font=self.font,borderwidth=self.borderwidth)
  self.mainmenu=Menu(self.widget,tearoff=self.tearoff,bg=self.bg,fg=self.fg,font=self.font)
  self._create_menu_lists()
  self.widget['menu']=self.mainmenu
 def _create_menu_lists(self):
  for menus in self.menu_lists:
   lens=len(menus)
   if not isinstance(menus,list):continue
   for i in range(0,lens,2):
    if lens<=i+1:break
    submenu=Menu(self.mainmenu,tearoff=self.tearoff,bg=self.bg,fg=self.fg,font=self.font)
    self._add_items_recursive(menu=submenu,items=menus[i+1])
    self.mainmenu.add_cascade(label=menus[i],menu=submenu)
 def _add_items_recursive(self,menu:Menu,items):
  i=0
  while i<len(items):
   item=items[i]
   if item=='---':
    menu.add_separator()
    i+=1
    continue
   if isinstance(item,dict):
    self.funcs=item.get('function')
    menu.add_command(label=item.get('label'),command=lambda f=self.funcs:self._exec_funcs(f))
    self.funcs=None
    i+=1
    continue
   if isinstance(item,str):
    if i+1<len(items) and isinstance(items[i+1],list):
     new_sub=Menu(menu,tearoff=self.tearoff,bg=self.bg,fg=self.fg,font=self.font)
     self._add_items_recursive(new_sub,items[i+1])
     menu.add_cascade(label=item,menu=new_sub)
     i+=2
     continue
    else:
     menu.add_command(label=item)
     i+=1
     continue
   if isinstance(item,list):
    new_sub=Menu(menu,tearoff=self.tearoff,bg=self.bg,fg=self.fg,font=self.font)
    self._add_items_recursive(new_sub,item)
    menu.add_cascade(label='Submenu',menu=new_sub)
    i+=1
    continue
 def get_items(self):return self.menu_lists
 def clear(self):
  self.mainmenu.delete(0,'end')
  self.menu_lists=[]
 def addmenu(self,label,submenu_lists):
  self.menu_lists.append([label,submenu_lists])
  self._create_menu_lists(self.menu_lists)
 def delta(self):
  try:self.widget.destroy()
  except Exception as e:
   logger.error(e)
 def get_text(self):
  try:
   return self.text
  except Exception as e:
   logger.error(e)
 def set_text(self,txt):
  try:
   self.text=txt
   self.widget.config(text=txt)
  except Exception as e:logger.error(e)
 def get_fg(self):
  try:return str(self.bg)
  except Exception as e:logger.error(e)
 def set_fg(self,fg):
  try:
   self.fg=fg
   self.widget.config(fg=fg)
  except Exception as e:logger.error(e)
 def get_bg(self):
  try:return str(self.bg)
  except Exception as e:logger.error(e)
 def set_bg(self,bg):
  try:
   self.bg=bg
   self.widget.config(bg=bg)
  except Exception as e:
   logger.error(e)
class Frames(Element):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.borderwidth=num0(kw.get('bd'),1)
  self.title=kw.get('title')
  self.relief=listchose(kw.get('relief'),['flat','raised','sunken','ridge','solid','groove'],'solid')
  self.labelanchor=listchose(kw.get('labelanchor'),['nw','n','ne','en','e','es','se','s','sw','ws','w','wn'])
  self.widget=LabelFrame(self.master,takefocus=self.takefocus,pady=self.pady,padx=self.padx,relief=self.relief,cursor=self.cursor,labelanchor=self.labelanchor,text=self.title,font=self.font,bg=self.bg,fg=self.fg,borderwidth=self.borderwidth)
 def delta(self):
  try:self.widget.destroy()
  except Exception as e:
   logger.error(e)
 def get_fg(self):
  try:return str(self.bg)
  except Exception as e:logger.error(e)
 def set_fg(self,fg):
  try:
   self.fg=fg
   self.widget.config(fg=fg)
  except Exception as e:logger.error(e)
 def get_bg(self):
  try:return str(self.bg)
  except Exception as e:logger.error(e)
 def set_bg(self,bg):
  try:
   self.bg=bg
   self.widget.config(bg=bg)
  except Exception as e:
   logger.error(e)
class Column(Element):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.widget=Frame(self.master,takefocus=self.takefocus,pady=self.pady,padx=self.padx,relief=self.relief,cursor=self.cursor,bg=self.bg,borderwidth=self.borderwidth)
 def delta(self):
  try:self.widget.destroy()
  except Exception as e:
   logger.error(e)
 def get_fg(self):
  try:return str(self.bg)
  except Exception as e:logger.error(e)
 def set_fg(self,fg):
  try:
   self.fg=fg
   self.widget.config(fg=fg)
  except Exception as e:logger.error(e)
 def get_bg(self):
  try:return str(self.bg)
  except Exception as e:logger.error(e)
 def set_bg(self,bg):
  try:
   self.bg=bg
   self.widget.config(bg=bg)
  except Exception as e:
   logger.error(e)
class Tab(Element):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  style=Style()
  self.stylename=f'Custom{kw.get('count')}.TNotebook'
  style.theme_use('default')
  style.configure(self.stylename,background=self.back_bg)
  style.configure(f'{self.stylename}.Tab',background=self.bg,foreground=self.fg,font=self.font)
  style.map(f'{self.stylename}.Tab',background=[('selected',('#cccccc'))])
  self.frames=[]
  self.widget=Notebook(self.master,takefocus=self.takefocus,style=self.stylename)
  self.widget.pack(side='left',padx=5,pady=5)
 def _add_tab(self,frame,title):
  self.widget.add(frame,text=title)
  self.frames.append(frame)
 def delta(self):
  try:self.widget.destroy()
  except Exception as e:
   logger.error(e)