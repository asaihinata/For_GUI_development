from typing import Literal, Unpack

from sgg._typing import Dict_P_Warning

__all__ = ["popupwarning", "popupwarningyesno"]

def popupwarning(
    **kwargs: Unpack[Dict_P_Warning],
) -> Literal["ok"]: ...
def popupwarningyesno(
    **kwargs: Unpack[Dict_P_Warning],
) -> Literal["yes", "no"]: ...
