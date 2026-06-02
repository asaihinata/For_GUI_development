from ..btn import *
__all__=['Savebtn']
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