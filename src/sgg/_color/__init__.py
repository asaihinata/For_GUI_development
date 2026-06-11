from ..nparray.npColor import NPColor
from .data import Get_color
__all__=['Color']
class Color:
 def __init__(self,color):
  colors=Get_color.gets(color)
  if colors is None:self.__color=NPColor(color)[0]
  else:self.__color=colors[1]
 def __repr__(self):return f'Color({self.__color})'
 @property
 def color(self):return str(self.__color)