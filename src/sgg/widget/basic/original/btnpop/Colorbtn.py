from tkinter import Button
from ...._dialog import askcolor
from ...._function import parsecolor
from .btn import Btn
__all__=['Colorbtn']
class Colorbtn(Btn):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.selectcolor=(None,None)
  self.color=parsecolor(kw.get('color'),'#ffffff')
  self.title=kw.get('title','select color')
  self.text=kw.get('text','select color')
  self.widget=Button(master,takefocus=self.takefocus,anchor=self.anchor,pady=self.pady,padx=self.padx,relief=self.relief,wraplength=self.wraplength,cursor=self.cursor,text=self.text,bg=self.bg,fg=self.fg,font=self.font,width=self.width,height=self.height,command=self.select_color,borderwidth=self.borderwidth)
 def select_color(self):self.selectcolor=askcolor(color=self.color,title=self.title)
 def _get_color(self):return self.selectcolor
 get_color=_get_color