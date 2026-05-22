from io import BytesIO
from tkinter import Label
from PIL.ImageTk import PhotoImage
from ...common import *
from ...dev import Img_byte
__all__=['Imagebyte']
class Imagebyte(Element):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.byte=kw.get('byte')
  if not isinstance(self.byte,bytes|BytesIO):
   raise TypeError('byteにはbytesもしくはBytesIOを指定してください')
  self.imgs=PhotoImage(image=Img_byte(self.byte).imgs)
  self.widget=Label(master,text=None,image=self.imgs,takefocus=self.takefocus)
  self.widget.image=self.imgs
 def delta(self):self.widget.destroy()