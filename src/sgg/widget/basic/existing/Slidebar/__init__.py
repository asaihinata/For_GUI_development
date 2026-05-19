from tkinter import Scale
from ...._function import listchose,num0,nums
from ...._log import Logger
from ....base import Element
logger=Logger(format={'filename':None,'lineno':{'after':'行目'},'message':None}).get_logger()
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
