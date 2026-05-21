from tkinter import LabelFrame
from ...common import *
class Frames(Element):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.borderwidth=num0(kw.get('bd'),1)
  self.title=kw.get('title')
  self.relief=listchose(kw.get('relief'),['flat','raised','sunken','ridge','solid','groove'],'solid')
  self.labelanchor=listchose(kw.get('labelanchor'),['nw','n','ne','en','e','es','se','s','sw','ws','w','wn'])
  self.widget=LabelFrame(self.master,takefocus=self.takefocus,pady=self.pady,padx=self.padx,relief=self.relief,cursor=self.cursor,labelanchor=self.labelanchor,text=self.title,font=self.font,bg=self.bg,fg=self.fg,borderwidth=self.borderwidth)
 def delta(self):self.widget.destroy()
 def get_fg(self):return str(self.bg)
 def set_fg(self,fg):
  self.fg=fg
  self.widget.config(fg=fg)
 def get_bg(self):return str(self.bg)
 def set_bg(self,bg):
  self.bg=bg
  self.widget.config(bg=bg)
