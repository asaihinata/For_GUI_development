from ..maindialog.Dialog import Dialog
class Directory(Dialog):
 command='tk_chooseDirectory'
 def _fixresult(self,widget,result):
  if result:
   try:result=result.string
   except:pass
   self.options['initialdir']=result
  self.directory=result
  return result
def askdirectory(**options):return Directory(**options).show()