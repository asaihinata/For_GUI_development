from tkinter import Frame
from ...common import *
class Column(Element):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.widget=Frame(self.master,takefocus=self.takefocus,pady=self.pady,padx=self.padx,relief=self.relief,cursor=self.cursor,bg=self.bg,borderwidth=self.borderwidth)
 def delta(self):self.widget.destroy()
 def get_fg(self):return str(self.bg)
 def set_fg(self,fg):
  self.fg=fg
  self.widget.config(fg=fg)
 def get_bg(self):return str(self.bg)
 def set_bg(self,bg):
  self.bg=bg
  self.widget.config(bg=bg)
