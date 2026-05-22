from tkinter import Label
from PIL.ImageTk import PhotoImage
from ...common import *
from ...dev import Img_byte
from .getdata import get_link_img
__all__=['Imagelink']
class Imagelink(Element):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.link=kw.get('link')
  self.imgs=PhotoImage(Img_byte(get_link_img(self.link)).asresize().imgs)
  self.widget=Label(master,text=None,image=self.imgs,takefocus=self.takefocus)
  self.widget.image=self.imgs
 def delta(self):self.widget.destroy()