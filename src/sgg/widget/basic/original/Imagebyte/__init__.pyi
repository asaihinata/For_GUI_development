from io import BytesIO
from tkinter import Label
from PIL.ImageTk import PhotoImage
from ....base import _Element
from .....typing import *
__all__=['Imagebyte']
class Imagebyte(_Element):
 byte:bytes|BytesIO
 imgs:PhotoImage
 widget:Label
 def delta(self):'''ウィジェットを削除する。'''