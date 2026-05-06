from matplotlib.text import Text
__all__=['Texts']
class Texts(Text):
 def __init__(
self,
x=0,
y=0,
text='',
color=None,
va='baseline',
ha='left',
ma=None,
fontproperties=None,
rotation=0.0,
linespacing=0,
rotation_mode='default',
usetex=False,
wrap=False,
transform_rotates_text=False,
parse_math=True,
antialiased=True,
**kwargs):
  self.x=x
  self.y=y
  self.text=text
  self.color=color
  self.va=va
  self.ha=ha
  self.ma=ma
  self.fontproperties=fontproperties
  self.rotation=rotation
  self.linespacing=linespacing
  self.rotation_mode=rotation_mode
  self.usetex=usetex
  self.wrap=wrap
  self.transform_rotates_text=transform_rotates_text
  self.parse_math=parse_math
  self.antialiased=antialiased
  for key,value in kwargs.items():setattr(self,key,value)
  super().__init__(
self.x,
self.y,
self.text,
color=self.color,
verticalalignment=self.va,
horizontalalignment=self.ha,
multialignment=self.ma,
fontproperties=self.fontproperties,
rotation=self.rotation,
linespacing=self.linespacing,
rotation_mode=self.rotation_mode,
usetex=self.usetex,
wrap=self.wrap,
transform_rotates_text=self.transform_rotates_text,
parse_math=self.parse_math,
antialiased=self.antialiased,
**kwargs)
 def get(self):return vars(self)