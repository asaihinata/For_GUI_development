from tkinter import Label
from PIL import ImageTk
from ....base import Element
from ...dev import Img_byte
__all__=['Imagebyto']
class Imagebyto(Element):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.byte=kw.get('byte')
  self.img=Img_byte(self.byte)
  self.imgs=ImageTk.PhotoImage(image=self.img.imgs.resize(self.img.get_size()))
  self.widget=Label(master,text=None,image=self.imgs,takefocus=self.takefocus)
  self.widget.image=self.imgs