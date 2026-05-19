from tkinter import Radiobutton,StringVar
from ...._function import num0
from ...._log import Logger
from ....base import Element
logger=Logger(format={'filename':None,'lineno':{'after':'行目'},'message':None}).get_logger()
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
