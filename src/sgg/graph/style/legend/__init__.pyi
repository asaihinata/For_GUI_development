from collections.abc import Iterable
from typing import Any,Literal
from matplotlib.artist import Artist
from matplotlib.axes._axes import Axes
from matplotlib.font_manager import FontProperties
from matplotlib.legend_handler import HandlerBase
from matplotlib.transforms import BboxBase,Transform
from mpl_toolkits.mplot3d.axes3d import Axes3D
from ...typing import ColorType,ColorTypeN
class Legends:
 def __init__(
self,
ax:Axes|Axes3D,
)->None:...