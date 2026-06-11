from .._color import Color
__all__=['parsecolor']
def parsecolor(val,other=None):
 if val is None:return other
 return Color(val).color