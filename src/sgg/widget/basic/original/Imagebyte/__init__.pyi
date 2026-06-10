from io import BytesIO
from tkinter import Label
from PIL.ImageTk import PhotoImage
from .....typing import *
from ....base import _Element
__all__=['Imagebyte']
class Imagebyte(_Element):
 byte:bytes|BytesIO
 imgs:PhotoImage
 widget:Label
 def delta(self):'''ウィジェットを削除する。'''