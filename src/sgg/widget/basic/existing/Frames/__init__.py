from tkinter import LabelFrame
from ...common import *
logger=Logger(format={'filename':None,'lineno':{'after':'行目'},'message':None}).get_logger()
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
