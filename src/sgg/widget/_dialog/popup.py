from .dialogs import Message
def _show(title=None,message=None,_icon=None,_type=None,**kw):
 if _icon and 'icon' not in kw:kw['icon']=_icon
 if _type and 'type' not in kw:kw['type']=_type
 if title:kw['title']=title
 if message:kw['message']=message
 res=Message(**kw).show()
 if isinstance(res,bool):return 'yes' if res else 'no'
 return str(res)
def showinfo(title=None,message=None,**kw):return _show(title,message,'info','ok',**kw)
def showwarning(title=None,message=None,**kw):return _show(title,message,'warning','ok',**kw)
def showerror(title=None,message=None,**kw):return _show(title,message,'error','ok',**kw)
def askquestion(title=None,message=None,**kw):return _show(title,message,'question','yesno',**kw)
def askokcancel(title=None,message=None,**kw):return _show(title,message,'question','okcancel',**kw)=='ok'
def askyesno(title=None,message=None,**kw):return _show(title,message,'question','yesno',**kw)=='yes'
def askretrycancel(title=None,message=None,**kw):return _show(title,message,'warning','retrycancel',**kw)=='retry'
def askyesnocancel(title=None,message=None,**kw):
 s=str(_show(title,message,'question','yesnocancel',**kw))
 return None if s=='cancel' else s=='yes'
def _iconset(icon,other='info'):
 if icon in ['info','error','warning','question']:return icon
 return other
class popups:
 def __init__(self,**kw):
  self.title=kw.get('title','Information')
  self.message=kw.get('message','Information message')
  self.icon=_iconset(kw.get('icon'),'info')
  self.retul=showinfo(title=self.title,message=self.message,icon=self.icon)
 def get_select(self):return self.retul
 def __str__(self):return str(self.retul)
class popupw:
 def get_select(self):return self.retul
 def __str__(self):return str(self.retul)
 def __init__(self,**kw):
  self.title=kw.get('title','Warning')
  self.message=kw.get('message','Warning message')
  self.icon=_iconset(kw.get('icon'),'warning')
  self.retul=showwarning(title=self.title,message=self.message,icon=self.icon)
class popupwyn:
 def get_select(self):return self.retul
 def __str__(self):return str(self.retul)
 def __init__(self,**kw):
  self.title=kw.get('title','Warning')
  self.message=kw.get('message','Warning message')
  self.icon=_iconset(kw.get('icon'),'warning')
  self.retul=showwarning(title=self.title,message=self.message,icon=self.icon,type='yesno')
class popupe:
 def get_select(self):return self.retul
 def __str__(self):return str(self.retul)
 def __init__(self,**kw):
  self.title=kw.get('title','Error')
  self.message=kw.get('message','Error message')
  self.icon=_iconset(kw.get('icon'),'error')
  self.retul=showerror(title=self.title,message=self.message,icon=self.icon)
class popupeyn:
 def get_select(self):return self.retul
 def __str__(self):return str(self.retul)
 def __init__(self,**kw):
  self.title=kw.get('title','Error')
  self.message=kw.get('message','Error message')
  self.icon=_iconset(kw.get('icon'),'error')
  self.retul=showerror(title=self.title,message=self.message,icon=self.icon,type='yesno')
class popupq:
 def __str__(self):return str(self.retul)
 def get_select(self):return self.retul
 def __init__(self,**kw):
  self.title=kw.get('title','Question')
  self.message=kw.get('message','Question message')
  self.icon=_iconset(kw.get('icon'),'question')
  self.retul=askquestion(title=self.title,message=self.message,icon=self.icon)
class popupoc:
 def get_select(self):return self.retul
 def __bool__(self):return bool(self.retul)
 def __init__(self,**kw):
  self.title=kw.get('title','Question')
  self.message=kw.get('message','Question message')
  self.icon=_iconset(kw.get('icon'),'question')
  self.retul=askokcancel(title=self.title,message=self.message,icon=self.icon)
class popupyn:
 def get_select(self):return self.retul
 def __bool__(self):return bool(self.retul)
 def __init__(self,**kw):
  self.title=kw.get('title','Question')
  self.message=kw.get('message','Question message')
  self.icon=_iconset(kw.get('icon'),'question')
  self.retul=askyesno(title=self.title,message=self.message,icon=self.icon)
class popupync:
 def get_select(self):return self.retul
 def __bool__(self):return bool(self.retul)
 def __init__(self,**kw):
  self.title=kw.get('title','Question')
  self.message=kw.get('message','Question message')
  self.icon=_iconset(kw.get('icon'),'question')
  self.retul=askyesnocancel(title=self.title,message=self.message,icon=self.icon)
class popuptry:
 def get_select(self):return self.retul
 def __bool__(self):return bool(self.retul)
 def __init__(self,**kw):
  self.title=kw.get('title','Question')
  self.message=kw.get('message','Question message')
  self.icon=_iconset(kw.get('icon'),'question')
  self.retul=askretrycancel(title=self.title,message=self.message,icon=self.icon)
def popup(title='Information',message='Information message',icon='info'):return popups(title=title,message=message,icon=icon).get_select()
def popupwarning(title='Warning',message='Warning message',icon='warning'):return popupw(title=title,message=message,icon=icon).get_select()
def popupwarningyesno(title='Warning',message='Warning message',icon='warning'):return popupwyn(title=title,message=message,icon=icon).get_select()
def popuperror(title='Error',message='Error message',icon='error'):return popupe(title=title,message=message,icon=icon).get_select()
def popuperroryesno(title='Error',message='Error message',icon='error'):return popupeyn(title=title,message=message,icon=icon).get_select()
def popupquestion(title='Question',message='Question message',icon='question'):return popupq(title=title,message=message,icon=icon).get_select()
def popupokcansel(title='Question',message='Question message',icon='question'):return popupoc(title=title,message=message,icon=icon).get_select()
def popupyesno(title='Question',message='Question message',icon='question'):return popupyn(title=title,message=message,icon=icon).get_select()
def popupyesnocansel(title='Question',message='Question message',icon='question'):return popupync(title=title,message=message,icon=icon).get_select()
def popuptrys(title='Question',message='Question message',icon='question'):return popuptry(title=title,message=message,icon=icon).get_select()