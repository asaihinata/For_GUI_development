from typing import Literal,TypeAlias
import numpy as np
from .....typing import *
__all__=['Type_NumberandNone','Type_Solid']
Type_NumberandNone:TypeAlias=Type_Number|None
Type_Solid=Literal['-','--','-.',':','None',' ','']