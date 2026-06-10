from .._color import Color

__all__=['parsecolor','wparsecolor']
def parsecolor(val,other=None):
 if val is None:return other
 return Color(val).color
def wparsecolor(val,other=None):
 if val is None:return other
 return Color(val,keep_alpha=False).color