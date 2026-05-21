from tkinter import Label
from PIL import ImageTk
from ...common import *
from ...dev import Img_byte
__all__=['Imagebyte']
class Imagebyte(Element):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.byte=kw.get('byte')
  self.img=Img_byte(self.byte)
  self.imgs=ImageTk.PhotoImage(image=self.img.imgs.resize(self.img.get_size()))
  self.widget=Label(master,text=None,image=self.imgs,takefocus=self.takefocus)
  self.widget.image=self.imgs
 def delta(self):self.widget.destroy()