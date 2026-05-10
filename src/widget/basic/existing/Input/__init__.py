from tkinter import Entry
from ...._function import num0,parsecolor
from ...._log import Logger
from ....base import Element
logger=Logger(name='template',format={'filename':None,'lineno':{'after':'行目'},'message':None}).get_logger()
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
