from os.path import abspath
from pathlib import Path
from tkinter import Label
from webbrowser import open

from ...._font import fonts
from ...common import *

__all__=['Link']
class Link(Element):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.underline=kw.get('underline',True)
  self.font=fonts(self.family,self.font_size,self.weight,self.slant,self.underline,self.overstrike,master)
  self.fg=parsecolor(kw.get('fg'),'#0000ee')
  self.wraplength=num0(kw.get('wraplength'))
  self.link_url=kw.get('link')
  self.text=kw.get('text')
  if self.text==None and self.link_url!=None:self.text=self.link_url
  elif self.text!=None and self.link_url==None:pass
  self.widget=Label(master,takefocus=self.takefocus,anchor=self.anchor,pady=self.pady,padx=self.padx,relief=self.relief,wraplength=self.wraplength,cursor=self.cursor,text=self.text,bg=self.bg,fg=self.fg,font=self.font,width=self.width,height=self.height,justify=self.justify,borderwidth=self.borderwidth)
  self.widget.bind('<Button-1>',self._link)
 def _link(self,ev):
  if self.link_url!=None:
   p=Path(self.link_url)
   if p.exists() and p.is_file() and p.suffix.lower() in ['.html','.htm']:open(Path(f'file://{abspath(self.link_url)}').resolve())
   else:
    try:open(self.link_url)
    except Exception as e:
     raise Exception(e)
 def delta(self):self.widget.destroy()
 def get_text(self):return self.text
 def set_text(self,txt):
  self.text=txt
  self.widget.config(text=txt)
 def get_link(self):return self.link_url
 def set_link(self,link):self.link_url=link
 def get_fg(self):return str(self.bg)
 def set_fg(self,fg):
  self.fg=fg
  self.widget.config(fg=fg)
 def get_bg(self):return str(self.bg)
 def set_bg(self,bg):
  self.bg=bg
  self.widget.config(bg=bg)