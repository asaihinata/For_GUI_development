from os.path import split
from tkinter import _destroy_temp_root, _get_temp_root


class Dialog:
 command=None
 def __init__(self,master=None,**options):
  if master==None:master=options.get('parent')
  self.master,self.options=master,options
 def _fixoptions(self):pass
 def _fixresult(self,widget,result):return result
 def show(self,**options):
  for k,v in options.items():self.options[k]=v
  self._fixoptions()
  master=self.master
  if master==None:master=_get_temp_root()
  try:
   self._test_callback(master)
   s=self._fixresult(master,master.tk.call(self.command,*master._options(self.options)))
  finally:_destroy_temp_root(master)
  return s
 def _test_callback(self,master):pass
class Directory(Dialog):
 command='tk_chooseDirectory'
 def _fixresult(self,widget,result):
  if result:
   try:result=result.string
   except:pass
   self.options['initialdir']=result
  self.directory=result
  return result
class Chooser(Dialog):
 command='tk_chooseColor'
 def _fixoptions(self):
  try:
   color=self.options['initialcolor']
   if isinstance(color,tuple):self.options['initialcolor']='#%02x%02x%02x'%color
  except:pass
 def _fixresult(self,widget,result):
  if not result or not str(result):return None,None
  r,g,b=widget.winfo_rgb(result)
  return(r//256,g//256,b//256),str(result)
class Message(Dialog):command='tk_messageBox'
class _Dialog(Dialog):
 def _fixoptions(self):
  try:self.options['filetypes']=tuple(self.options['filetypes'])
  except:pass
 def _fixresult(self,widget,result):
  if result:
   try:result=result.string
   except:pass
   path,file=split(result)
   self.options['initialdir']=path
   self.options['initialfile']=file
  self.filename=result
  return result
class SaveAs(_Dialog):command='tk_getSaveFile'
class Open(_Dialog):
 command='tk_getOpenFile'
 def _fixresult(self,widget,result):
  if isinstance(result,tuple):
   result=tuple([getattr(r,'string',r)for r in result])
   if result:
    path,_=split(result[0])
    self.options['initialdir']=path
   return result
  if not widget.tk.wantobjects()and 'multiple' in self.options:return self._fixresult(widget,widget.tk.splitlist(result))
  return _Dialog._fixresult(self,widget,result)
def askopenfilename(**options):return Open(**options).show()
def asksaveasfilename(**options):return SaveAs(**options).show()
def askdirectory(**options):return Directory(**options).show()
def askcolor(color=None,**options):
 if color:options,options['initialcolor']=options.copy(),color
 return Chooser(**options).show()