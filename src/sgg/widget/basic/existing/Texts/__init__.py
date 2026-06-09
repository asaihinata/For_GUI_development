from tkinter import Label
from ...common import *
__all__=['Texts']
class Texts(Element):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.wraplength=num0(kw.get('wraplength'))
  self.text=kw.get('text')
  self.widget=Label(self.master,takefocus=self.takefocus,borderwidth=self.borderwidth,anchor=self.anchor,pady=self.pady,padx=self.padx,relief=self.relief,wraplength=self.wraplength,cursor=self.cursor,text=self.text,bg=self.bg,fg=self.fg,font=self.font,width=self.width,height=self.height,justify=self.justify)
 def delta(self):self.widget.destroy()
 def get_text(self):return self.text
 def set_text(self,txt):
  self.text=txt
  self.widget.config(text=txt)
 def get_fg(self):return str(self.bg)
 def set_fg(self,fg):
  self.fg=fg
  self.widget.config(fg=fg)
 def get_bg(self):return str(self.bg)
 def set_bg(self,bg):
  self.bg=bg
  self.widget.config(bg=bg)