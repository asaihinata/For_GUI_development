from tkinter import Scale
from ...common import *
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
 def delta(self):self.widget.destroy()
 def get_fg(self):return str(self.bg)
 def set_fg(self,fg):
  self.fg=fg
  self.widget.config(fg=fg)
 def get_bg(self):return str(self.bg)
 def set_bg(self,bg):
  self.bg=bg
  self.widget.config(bg=bg)
