from io import BytesIO
from tkinter import Label
from barcode import get_barcode_class
from barcode.writer import ImageWriter
from PIL import ImageTk
from qrcode import make
from ..._log import Logger
from ...base import Element
from ._photo import Photo
__all__=['Barcode','Images','QRcode']
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
class QRcode(Element):
 def __init__(self,master,kw:dict):
  super().__init__(master,kw)
  self.text=kw.get('text')
  self.names=kw.get('name','No Qrcode image')
  self.img=make(self.text)
  self.sizes=self.img.size
  if self.sizes and isinstance(self.sizes,tuple):self.img=self.img.resize(self.sizes)
  self.image=ImageTk.PhotoImage(self.img)
  try:
   self.widget=Label(master,image=self.image,takefocus=self.takefocus)
   self.widget.image=self.image
  except Exception as e:
   logger.error(f'error:{e}')
   self.widget=Label(master,text=self.names,fg='#000000',takefocus=self.takefocus,bg=self.bg)
 def delta(self):
  try:self.widget.destroy()
  except Exception as e:
   logger.error(e)
class Barcode(Element):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.master=master
  self.data=kw.get('data')
  self.data_type=kw.get('data_type','Code128')
  self.names=kw.get('name','No Barcode image')
  for k,v in {'EAN-8':'ean8','EAN-13':'ean13','JAN':'jan','Code39':'code39','Code128':'code128'}.items():
   if self.data_type==k:
    self.set,self.item=k,v
    break
  else:self.set,self.item='Code128','code128'
  try:
   barclass=BytesIO()
   get_barcode_class(self.item)(str(self.data),writer=ImageWriter()).write(barclass)
   barclass.seek(0)
   (self.path,self.imgs,self.imgdate)=Photo(barclass).data()
   self.widget=Label(self.master,image=self.path,takefocus=self.takefocus)
   self.widget.image=self.path
  except Exception as e:
   logger.error(f'error:{e}')
   self.widget=Label(self.master,text=self.names,bg=self.bg,fg='#000000',takefocus=self.takefocus)
 def delta(self):
  try:self.widget.destroy()
  except Exception as e:
   logger.error(e)