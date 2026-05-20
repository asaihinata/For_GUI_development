'''popup用の型ヒント'''
from tkinter import Misc
from typing import Literal,TypeAlias
__all__=['Misc','Type_icon','Type_ok','Type_yn','Type_oc','Type_cyn','Type_rc']
Type_icon:TypeAlias=Literal["error", "info", "question", "warning"]
Type_ok:TypeAlias=Literal["ok"]
Type_yn:TypeAlias=Literal["yes", "no"]
Type_oc:TypeAlias=Literal["ok", "cancel"]
Type_cyn:TypeAlias=Literal["cancel", "yes", "no"]
Type_rc:TypeAlias=Literal["retry", "cancel"]