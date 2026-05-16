from tkinter import Label
from ...._log import Logger
from ....base import Element
from ...dev import Photo
__all__=['Images']
logger=Logger(name='image',format={'filename':None,'lineno':{'after':'行目'},'message':None}).get_logger()
class Images(Element):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.file=kw.get('path')
  self.byto=kw.get('byto')
  self.names=kw.get('name','No Images')
  self.size=self.width,self.height
  if self.byto==None and self.file==None:
   logger.warning('path and byto is None')
  if self.byto!=None and not isinstance(self.byto,bytes):
   logger.warning('byto\'s type isn\'t bytes type')
  if self.file!=None and not isinstance(self.file,str):
   logger.warning('path\'s type isn\'t str type')
  if (self.byto!=None and self.file!=None) or (self.byto!=None and isinstance(self.byto,bytes)) or (self.file!=None and isinstance(self.file,str)):
   getdata=Photo(file=(self.byto if not self.file and self.byto else self.file),size=self.size)
   (self.path,self.imgs,self.imgdate)=getdata.data()
  try:
   self.widget=Label(master,text=None,image=self.path,takefocus=self.takefocus)
   self.widget.image=self.path
  except Exception as e:
   logger.error(f'error:{e}')
   self.widget=Label(master,text=self.names,fg='#000000',takefocus=self.takefocus)
 def delta(self):
  try:self.widget.destroy()
  except Exception as e:
   logger.error(e)
