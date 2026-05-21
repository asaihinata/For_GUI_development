from tkinter import Label
from PIL import ImageTk
from ...common import *
from ...dev import Img_byte
from .barcodes import barcode_data
__all__=['Barcode']
class Barcode(Element):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.master=master
  self.data=kw.get('data','')
  self.format=kw.get('format','code39')
  self.barcode=barcode_data(self.data,self.format)
  self.img=Img_byte(self.barcode.bytedata)
  self.imgs=ImageTk.PhotoImage(image=self.img.imgs.resize(self.img.get_size()))
  self.widget=Label(master,text=None,image=self.imgs,takefocus=self.takefocus)
  self.widget.image=self.imgs
 def delta(self):self.widget.destroy()