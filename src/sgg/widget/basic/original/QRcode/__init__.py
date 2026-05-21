from tkinter import Label
from PIL import ImageTk
from qrcode import make
from ...common import *
__all__=['QRcode']
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
  except:
   self.widget=Label(master,text=self.names,fg='#000000',takefocus=self.takefocus,bg=self.bg)
 def delta(self):self.widget.destroy()