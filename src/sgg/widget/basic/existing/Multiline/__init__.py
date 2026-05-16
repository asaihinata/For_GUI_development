from tkinter import Text
from ...._function import listchose,num0,parsecolor
from ...._log import Logger
from ....base import Element
logger=Logger(name='template',format={'filename':None,'lineno':{'after':'行目'},'message':None}).get_logger()
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
