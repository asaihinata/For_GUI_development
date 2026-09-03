from typing import Literal, Unpack

from sgg._typing import Dict_P_Error

__all__ = ["popuperror", "popuperroryesno"]

def popuperror(
    **kwargs: Unpack[Dict_P_Error],
) -> Literal["ok"]: ...
def popuperroryesno(
    **kwargs: Unpack[Dict_P_Error],
) -> Literal["yes", "no"]: ...
