'''widget/graph/Graph/style/composite内の型ヒントを設定しているモジュール'''
from typing import TypeAlias
from .....typing import *
__all__=['marKer','Type_Marker','Type_NumberandNone','Type_Solid']
Type_NumberandNone:TypeAlias=Type_Number|None
Type_Solid=Literal['-','--','-.',':','None',' ','']
marKer=['.',',','o','v','^','<','>','1','2','3','4','8','s','p','*','h','H','+','x','D','d','|','_','P','X',0,1,2,3,4,5,6,7,8,9,10,11,'None','none',' ','']
Type_Marker:TypeAlias=Literal['.',',','o','v','^','<','>','1','2','3','4','8','s','p','*','h','H','+','x','D','d','|','_','P','X',0,1,2,3,4,5,6,7,8,9,10,11,'None','none',' ','']