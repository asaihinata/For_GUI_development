from os import getcwd
from tkinter import Button
from ...._dialog import askcolor,askdirectory,askopenfilename,asksaveasfilename
from ...._function import listchose,num0,parsecolor
from ...._log import Logger
from ....base import Element
logger=Logger(format={'filename':None,'lineno':{'after':'行目'},'message':None}).get_logger()
__all__=['Colorbtn','FileLoad','FolderLoad','Savebtn']
class Btn(Element):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.anchor=listchose(kw.get('anchor'),['center','w','n','s','e','nw','ne','se','sw'])
  self.bg=parsecolor(kw.get('bg'),'#e0e0e0')
  self.wraplength=num0(kw.get('wraplength'))
 def dgettitle(self):return self.title
 def dsettitle(self,titles:str):self.title=titles
 def delta(self):
  try:self.widget.destroy()
  except Exception as e:
   logger.error(e)
 def get_text(self):
  try:
   return self.text
  except Exception as e:
   logger.error(e)
 def set_text(self,txt):
  try:
   self.text=txt
   self.widget.config(text=txt)
  except Exception as e:logger.error(e)
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
class FolderLoad(Btn):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.foldersaves=None
  self.title=kw.get('title','select Folder')
  self.text=kw.get('text','select Folder')
  self.widget=Button(master,takefocus=self.takefocus,anchor=self.anchor,pady=self.pady,padx=self.padx,relief=self.relief,wraplength=self.wraplength,cursor=self.cursor,text=self.text,bg=self.bg,fg=self.fg,font=self.font,width=self.width,height=self.height,command=self._choosefolder,borderwidth=self.borderwidth)
 def _choosefolder(self):
  self.foldersaves=askdirectory(title=self.title,initialdir=getcwd())
  return self.foldersaves
 def get_path(self):return self.foldersaves
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
class Savebtn(Btn):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.select_file=None
  self.text=kw.get('text','Save file')
  self.title=kw.get('title','Save file')
  self.defaultextension=kw.get('defaultextension','.txt')
  self.filetypes=kw.get('filetypes',[('All files','*.*')])
  self.initialfile=kw.get('initialfile')
  self.initialdir=kw.get('initialdir')
  self.widget=Button(master,takefocus=self.takefocus,anchor=self.anchor,pady=self.pady,padx=self.padx,relief=self.relief,wraplength=self.wraplength,cursor=self.cursor,text=self.text,bg=self.bg,fg=self.fg,font=self.font,width=self.width,height=self.height,command=self._savefile,borderwidth=self.borderwidth)
 def _savefile(self):
  self.select_file=asksaveasfilename(parent=self.master,initialfile=self.initialfile,initialdir=self.initialdir,defaultextension=self.defaultextension,filetypes=self.filetypes,title=self.title)
  return self.select_file
 def get_path(self):return self.select_file
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