from io import BytesIO
from tkinter import Label
from barcode import get_barcode_class
from barcode.writer import ImageWriter
from ...._log import Logger
from ....base import Element
from ...dev import Photo
__all__=['Barcode']
logger=Logger(name='barcode',format={'filename':None,'lineno':{'after':'行目'},'message':None}).get_logger()
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