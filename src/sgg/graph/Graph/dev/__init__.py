import japanize_matplotlib
import numpy as np
from ....dev import *
from ....nparray import *
from ...Element import RadarElement,polarElement,radar_factory,threeElement,twoElement
from ...Element.Graph import getLabel
from ...style import *
from ...typing import *
def parameters(vals,do1,do2):
 if vals==None:return do1
 return do2