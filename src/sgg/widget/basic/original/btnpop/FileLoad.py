from os import getcwd
from tkinter import Button
from ....._dialog import askopenfilename
from .btn import Btn
__all__=['FileLoad']
class FileLoad(Btn):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.filesaves=None
  self.text=kw.get('text','select File')
  self.title=kw.get('title','select File')
  self.widget=Button(master,takefocus=self.takefocus,anchor=self.anchor,pady=self.pady,padx=self.padx,relief=self.relief,wraplength=self.wraplength,cursor=self.cursor,text=self.text,bg=self.bg,fg=self.fg,font=self.font,width=self.width,height=self.height,command=self._choosefile,borderwidth=self.borderwidth)
 def _choosefile(self):
  self.filesaves=askopenfilename(title=self.title,initialdir=getcwd())
  return self.filesaves
 def get_path(self):return self.filesaves