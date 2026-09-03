from typing import Literal, Unpack

from sgg._typing import Dict_P_Information

__all__ = ["popup"]

def popup(
    **kwargs: Unpack[Dict_P_Information],
) -> Literal["ok"]: ...
