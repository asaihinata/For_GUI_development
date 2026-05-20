from tkinter import BooleanVar,Checkbutton
from ....dev import bols,num0
from ...._log import Logger
from ....base import Element
logger=Logger(format={'filename':None,'lineno':{'after':'行目'},'message':None}).get_logger()
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
