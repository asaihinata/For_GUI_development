from tkinter import Label
from PIL import ImageTk
from ....base import Element
from ...dev import Img_path
__all__=['Images']
class Images(Element):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.path=kw.get('path')
  self.img=Img_path(self.path)
  self.imgs=ImageTk.PhotoImage(image=self.img.imgs.resize(self.img.get_size()))
  self.widget=Label(master,text=None,image=self.imgs,takefocus=self.takefocus)
  self.widget.image=self.imgs