from tkinter import Label
from PIL import ImageGrab,ImageTk
from pyautogui import position,size
from ..._function import listchose,num0,num0s
from ..._log import Logger
from ...base import Element
logger=Logger(name='expansion',format={'filename':None,'lineno':{'after':'行目'},'message':None}).get_logger()
screenwidth,screenheight=size()
class Expansion(Element):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.range=self._range(kw.get('range'))
  self.time=num0s(kw.get('time'),50)
  self.width,self.height=self._sizes(kw.get('size'))
  self.local=self._local(kw.get('local'))
  self.locals=True if self.local==None else False
  self.borderwidth=num0(kw.get('bd'),2)
  self.relief=listchose(kw.get('relief'),['solid','flat','raised','sunken','ridge','groove'])
  self.widget=Label(master,border=self.borderwidth,relief=self.relief,width=self.width,height=self.height,cursor=self.cursor,padx=self.padx,pady=self.pady,takefocus=self.takefocus)
  self._update()
 def _local(self,val):
  if isinstance(val,(int,float)) and 0<val:return(val,val)
  elif isinstance(val,(list,tuple)) and len(val)==2 and (isinstance(i,(int,float))for i in val):return val
  return None
 def _range(self,val):
  if isinstance(val,(list,tuple)) and all(isinstance(i,(int,float))for i in val):
   if len(val)==2:return(val[0],val[0],val[1],val[1])
   elif len(val)==4:return val
  elif isinstance(val,(int,float)):return(val,val,val,val)
  return(30,30,30,30)
 def _sizes(self,size):
  if isinstance(size,(list,tuple)) and len(size)==2 and all(isinstance(i,(int,float))for i in size):return size
  return(300,300)
 def _update(self):
  if self.locals:
   self.ids=self.master.after(self.time,self._update)
   xys=position()
   self.x1,self.y1,self.x2,self.y2=xys.x-self.range[0],xys.y-self.range[1],xys.x+self.range[2],xys.y+self.range[3]
  else:
   x,y=self.local
   self.x1,self.y1,self.x2,self.y2=x-self.range[0],y-self.range[1],x+self.range[2],y+self.range[3]
  if self.x1<0:self.x2,self.x1=self.x2+abs(self.x1),0
  if self.y1<0:self.y2,self.y1=self.y2+abs(self.y1),0
  if screenheight<self.y2:self.y2=screenheight
  if screenwidth<self.x2:self.x2=screenwidth
  ph=ImageTk.PhotoImage(ImageGrab.grab((self.x1,self.y1,self.x2,self.y2)).resize((self.width,self.height)))
  self.widget.config(image=ph)
  self.widget.image=ph
 def delta(self):
  try:
   self.widget.destroy()
   if self.ids:self.master.after_cancel(self.ids)
  except Exception as e:
   logger.error(e)