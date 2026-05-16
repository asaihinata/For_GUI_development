from tkinter import Frame
from ...._log import Logger
from ....base import Element
logger=Logger(name='template',format={'filename':None,'lineno':{'after':'行目'},'message':None}).get_logger()
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
