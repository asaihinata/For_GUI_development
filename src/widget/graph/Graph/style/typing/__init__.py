from typing import Literal,TypeAlias
import numpy as np
from matplotlib.typing import ColorType
__all__=['ColorType','Type_Number','Type_NumberandNone','Type_Numberlike','Type_Solid']
Type_Number:TypeAlias=int|float
Type_NumberandNone:TypeAlias=Type_Number|None
Type_Numberlike:TypeAlias=bool|np.bool|Type_Number|np.float16|np.float32|np.float64|np.int16|np.int32|np.int64|np.int8|np.uint16|np.uint32|np.uint64|np.uint8
Type_Solid=Literal['-','--','-.',':','None',' ','']
Type_Color:TypeAlias=ColorType|None