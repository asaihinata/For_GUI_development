from tkinter import Label
from PIL import ImageTk
from ...common import *
from ...dev import Img_byte
from .getdata import get_link_img
__all__=['Imagelink']
class Imagelink(Element):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.link=kw.get('link')
  self.bytedata=get_link_img(self.link)
  self.img=Img_byte(self.bytedata)
  self.imgs=ImageTk.PhotoImage(image=self.img.imgs.resize(self.img.get_size()))
  self.widget=Label(master,text=None,image=self.imgs,takefocus=self.takefocus)
  self.widget.image=self.imgs
 def delta(self):self.widget.destroy()