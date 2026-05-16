from re import findall
from tkinter import Misc
from ..widget.typing import FunctionType
from ..widget._font import fonts
from ..widget._function import bols,listchose,num0,wparsecolor
from ..widget._log import Logger
__all__=['Element']
logger=Logger(name='base',format={'filename':None,'lineno':{'after':'行目'},'message':None}).get_logger()
class Element:
 def __init__(self,master:Misc,kw):
  self.widget,self.master,self.graph=None,master,False
  self.cursor=kw.get('cursor')
  self.back_bg=kw.get('back_bg')
  self.justify=listchose(kw.get('justify'),['left','right','center'])
  self.padx=num0(kw.get('padx'),1)
  self.pady=num0(kw.get('pady'),1)
  self.relief=listchose(kw.get('relief'),['flat','raised','sunken','ridge','solid','groove'])
  self.fg=wparsecolor(kw.get('fg'),'#000000')
  self.bg=wparsecolor(kw.get('bg'),'#64778d' if self.back_bg==None else self.back_bg)
  self.borderwidth=num0(kw.get('bd'))
  self.takefocus=bols(kw.get('takefocus'))
  self.family=kw.get('family')
  self.font_size=kw.get('font_size')
  self.weight=kw.get('weight')
  self.slant=kw.get('slant')
  self.underline=kw.get('underline')
  self.overstrike=kw.get('overstrike')
  self.font=fonts(self.family,self.font_size,self.weight,self.slant,self.underline,self.overstrike,self.master)
  self.anchor=listchose(kw.get('anchor'),['w','n','s','e','nw','ne','se','sw','center'])
  self.width,self.height=self._size(kw.get('size'))
 def _size_width(self,val,other=None):return(val if isinstance(val,int|float)else other)
 def _size_height(self,val,other=None):return(val if isinstance(val,int|float)else other)
 def _size(self,size,other=(None,None)):
  if isinstance(size,list|tuple) and len(size)==2 and (all(isinstance(i,int|float)for i in size) or (isinstance(size[0],int|float) and size[1] is None) or (isinstance(size[1],int|float) and size[0] is None)):return size
  return other
 def _exec_funcs(self,funcs=None):
  if isinstance(funcs,FunctionType):
   try:funcs()
   except Exception as e:
    logger.error(f'function({funcs.__name__}) error.\n{e}')
  elif isinstance(funcs,list|tuple):
   for f in funcs:
    if isinstance(f,FunctionType):
     try:f()
     except Exception as e:
      logger.error(f'function({funcs.__name__}) error.\n{e}')
    else:
     logger.warning(f'{f} is not function type')
  else:return None
 def winsize(self):
  root=self.master
  return root.winfo_width(),root.winfo_height()
 def winwidth(self):return self.master.winfo_width()
 def winheight(self):return self.master.winfo_height()
 def winxy(self):
  root=self.master
  return root.winfo_x(),root.winfo_y()
 def winx(self):return self.master.winfo_x()
 def winy(self):return self.master.winfo_y()
 def geometry(self):return[float(i) for i in findall(r'\d+',self.master.winfo_geometry())]
 def rootxy(self):
  root=self.master
  return root.winfo_rootx(),root.winfo_rooty()
 def rootx(self):return self.master.winfo_rootx()
 def rooty(self):return self.master.winfo_rooty()
 def visual(self):return self.master.winfo_visual()
 def screen(self):return self.master.winfo_screen()
 def reqsize(self):
  root=self.master
  return root.winfo_reqwidth(),root.winfo_reqheight()
 def reqwidth(self):return self.master.winfo_reqwidth()
 def reqheight(self):return self.master.winfo_reqheight()
 def id(self):return self.master.winfo_id()
 def name(self):return self.master.winfo_name()