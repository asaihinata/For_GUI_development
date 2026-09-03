from typing import Literal, Unpack

from sgg._typing import Dict_P_Question

__all__ = [
    "popupokcansel",
    "popupquestion",
    "popuptrys",
    "popupyesno",
    "popupyesnocansel",
]

def popupokcansel(
    **kwargs: Unpack[Dict_P_Question],
) -> bool: ...
def popupquestion(
    **kwargs: Unpack[Dict_P_Question],
) -> Literal["yes", "no"]: ...
def popuptrys(
    **kwargs: Unpack[Dict_P_Question],
) -> bool: ...
def popupyesno(
    **kwargs: Unpack[Dict_P_Question],
) -> bool: ...
def popupyesnocansel(
    **kwargs: Unpack[Dict_P_Question],
) -> bool | None: ...
