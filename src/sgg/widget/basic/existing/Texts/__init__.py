from tkinter import Label
from ....dev import num0
from ...._log import Logger
from ....base import Element
logger=Logger(format={'filename':None,'lineno':{'after':'行目'},'message':None}).get_logger()
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