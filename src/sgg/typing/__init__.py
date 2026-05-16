'''sggクラス専用の型ヒント'''
from typing import Literal,TypeAlias
__all__=['Type_legendplace','Type_orientation','Type_ticksdirection','Type_labelha','Type_labelva']
Type_legendplace:TypeAlias=Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
Type_orientation:TypeAlias=Literal['horizontal','vertical']
Type_ticksdirection:TypeAlias=Literal['out','in','inout']
Type_labelha:TypeAlias=Literal['left','center','right']|None
Type_labelva:TypeAlias=Literal['bottom','baseline','center','center_baseline','top']|None