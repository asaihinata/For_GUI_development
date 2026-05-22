from os import getcwd
from ..Btn import *
__all__=['FolderLoad']
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