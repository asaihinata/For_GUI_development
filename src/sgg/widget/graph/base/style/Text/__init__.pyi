from matplotlib.text import Text
from matplotlib.transforms import IdentityTransform
from .. import Color
class Texts(Text):
 def __init__(
self,
x=0,
y=0,
text='',
c=None,
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
**kwargs
):...